%if 0%{?rhel}
%global with_python3 0
%else
%global with_python3 1
%endif

%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

%global srcname pytest-sourceorder
%global modulename pytest_sourceorder
%global srcversion 0.3
%global versionedname %{srcname}-%{srcversion}

Name: python-%{srcname}
Version: %{srcversion}
Release: 1%{?dist}
Summary: Test-ordering plugin for pytest

License: GPLv3+
URL: https://github.com/encukou/%{srcname}

Source0: https://github.com/encukou/%{srcname}/archive/v%{srcversion}.tar.gz#/%{versionedname}.tar.gz

BuildArch: noarch
BuildRequires: python-devel
BuildRequires: python-setuptools
%if 0%{?with_python3}
BuildRequires: python3-devel
BuildRequires: python3-setuptools
%endif

Requires: python
Requires: pytest

%if 0%{?fedora}
# These are not *strictly* required, but are part of the default workflow.
Requires: PyYAML
Requires: python-paramiko
%endif


%description
Allows tests within a specially marked class to be run in source order,
instead of the "almost alphabetical" order Pytest normally uses.

%if 0%{?with_python3}
%package -n python3-%{srcname}
Summary: Test-ordering plugin for pytest

Requires: python3
Requires: python3-pytest

%description -n python3-%{srcname}
Allows tests within a specially marked class to be run in source order,
instead of the "almost alphabetical" order Pytest normally uses.

%endif


%prep
%setup -q -n %{versionedname}

%if 0%{?with_python3}
echo %{py3dir}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif


%build
%{__python2} setup.py build

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif

%install
%{__python2} setup.py install --skip-build --root %{buildroot}
%if 0%{?with_python3}
%py_byte_compile %{__python2} %{buildroot}%{python_sitelib}/%{srcname}
%else
# py_byte_compile is only defined in python3-devel
%{__python2} -m compileall %{buildroot}%{python_sitelib}/%{srcname}
%endif

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
%py_byte_compile %{__python3} %{buildroot}%{python3_sitelib}/%{srcname}
popd
%endif

%files
%doc COPYING
%doc README.rst
%{python_sitelib}/%{modulename}-%{version}-py2.?.egg-info
%{python_sitelib}/%{modulename}/

%if 0%{?with_python3}
%files -n python3-%{srcname}
%doc COPYING
%doc README.rst
%{python3_sitelib}/%{modulename}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{modulename}/
%endif


%changelog
* Wed Nov 26 2014 Petr Viktorin <encukou@gmail.com> - 0.3-1
- "Upstream" packaging fixes

* Mon Nov 10 2014 Petr Viktorin <encukou@gmail.com> - 0.2-1
- better extensibility
- bug fixes

* Mon Nov 10 2014 Petr Viktorin <encukou@gmail.com> - 0.1-1
- initial public version of package
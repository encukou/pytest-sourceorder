A pytest plugin for ensuring tests within a class are run in source order.


Downloading
-----------

Release tarballs will be made available for download from Fedora Hosted:
    https://fedorahosted.org/released/python-pytest-sourceorder/

The goal is to include this project in Fedora repositories. Until that happens,
you can use testing builds from COPR – see "Developer links" below.

You can also install using pip:
    https://pypi.python.org/pypi/pytest-sourceorder


Usage
-----

When installed, test classes marked ``@pytest_sourceorder.ordered`` will
have tests tun in the order of their definition.

Methods are ordered by line nuber of their definition, so spreading them
between multiple files or otherwise defining them outside of their class
might cause the plugin to order them wrong.

When inheriting from an ordered test class, the superclass' methods will be
run first (even if overridden), followed by the ones from subclasses.
You generally do *not* want to apply an additional ``@ordered`` decorator
to the subclasses – doing so will reset the inheritance-based ordering.


Contributing
------------

The project is happy to accept patches!
Please format your contribution using the FreeIPA `patch guidelines`_,
and send it to <freeipa-devel@redhat.com>.
Any development discussion is welcome there.

Someday the project might get its own list, but that seems premature now.


Developer links
---------------

  * Bug tracker: https://fedorahosted.org/python-pytest-sourceorder/report/3
  * Code browser: https://git.fedorahosted.org/cgit/python-pytest-sourceorder
  * git clone https://git.fedorahosted.org/git/python-pytest-sourceorder.git
  * Unstable packages for Fedora: https://copr.fedoraproject.org/coprs/pviktori/pytest-plugins/

To release, update version in setup.py, add a Git tag like "v0.3",
and run `make tarball`.
Running `make upload` will put the tarball to Fedora Hosted and PyPI,
and a SRPM on Fedorapeople, if you have the rights.
Running `make release` will upload and fire a COPR build.

.. _patch guidelines: http://www.freeipa.org/page/Contribute/Patch_Format

A pytest plugin for ensuring tests within a class are run in source order.


Downloading
-----------

Release tarballs will be made available for download from Pagure Releases:
    https://pagure.io/releases/python-pytest-sourceorder/

You can also install using pip:
    https://pypi.python.org/pypi/pytest-sourceorder

The plugin is also available in Fedora repositories as
``python3-pytest-sourceorder``.


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
Please file any patches as Pull Requests on the project's `Pagure repo`_.
Any development discussion should be in Pagure Pull Requests and Issues.


Developer links
---------------

  * Bug tracker: https://pagure.io/python-pytest-sourceorder/issues
  * Code browser: https://pagure.io/python-pytest-sourceorder/tree/master
  * git clone https://pagure.io/python-pytest-sourceorder.git
  * Unstable packages for Fedora: https://copr.fedoraproject.org/coprs/pviktori/pytest-plugins/

To release, update version in setup.py, add a Git tag like "v0.3",
and run `make tarball`.
Running `make upload` will put the tarball to Fedora Hosted and PyPI,
and a SRPM on Fedorapeople, if you have the rights.
Running `make release` will upload and fire a COPR build.

.. _Pagure repo: https://pagure.io/python-pytest-sourceorder

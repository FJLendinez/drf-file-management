=============================
DRF File management
=============================
.. image:: https://readthedocs.org/projects/drf-file-management/badge/?version=latest
    :target: https://drf-file-management.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://travis-ci.org/fjlendinez/drf-file-management.svg?branch=master
    :target: https://travis-ci.org/fjlendinez/drf-file-management

.. image:: https://codecov.io/gh/fjlendinez/drf-file-management/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/fjlendinez/drf-file-management

Small package to manage uploads and downloads in a centriliced way

Documentation
-------------

The full documentation is at https://drf-file-management.readthedocs.io.

Quickstart
----------

Install DRF File management::

    pip install git+https://github.com/FJLendinez/drf-file-management.git

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'drf_file_management',
        ...
    )

Add DRF File management's URL patterns:

.. code-block:: python

    from drf_file_management import urls as drf_file_management_urls


    urlpatterns = [
        ...
        url(r'^', include(drf_file_management_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage

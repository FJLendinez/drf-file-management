=====
Usage
=====

To use DRF File management in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'drf_file_management.apps.DrfFileManagementConfig',
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

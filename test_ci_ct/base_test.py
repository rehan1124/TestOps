import pytest


@pytest.mark.usefixtures("app_url", "find_by_status", "store_get_inventory")
class BaseTest:
    pass

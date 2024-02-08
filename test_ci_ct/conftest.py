import pytest

from shared.read_config import read_config


@pytest.fixture()
def app_url(request):
    base_url = read_config("DEFAULT", "Url")
    request.cls.base_url = base_url
    yield base_url


@pytest.fixture()
def find_by_status(request):
    find_by_status_url = read_config("PETS", "FindByStatus")
    request.cls.find_by_status_url = find_by_status_url
    yield find_by_status_url


@pytest.fixture()
def store_get_inventory(request):
    store_get_inventory_url = read_config("STORE", "GetInventory")
    request.cls.store_get_inventory_url = store_get_inventory_url
    yield store_get_inventory_url

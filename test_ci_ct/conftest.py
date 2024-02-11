import pytest

from shared.read_config import read_config


@pytest.fixture()
def app_url(request):
    base_url = read_config("DEFAULT", "url")
    request.cls.base_url = base_url
    yield base_url


@pytest.fixture()
def find_by_status(request):
    find_by_status_url = read_config("PETS", "find_by_status")
    request.cls.find_by_status_url = find_by_status_url
    yield find_by_status_url


@pytest.fixture()
def store_get_inventory(request):
    store_get_inventory_url = read_config("STORE", "get_inventory")
    request.cls.store_get_inventory_url = store_get_inventory_url
    yield store_get_inventory_url

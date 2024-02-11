import pytest
from pytest_check import check

import requests

from test_ci_ct.base_test import BaseTest


class TestPets(BaseTest):
    @pytest.mark.parametrize("status", ["available", "pending", "sold"])
    @pytest.mark.pets
    def test_find_pets_by_status(self, status):
        response = requests.get(url=self.base_url + self.find_by_status_url, params={"status": status})

        with check:
            assert response.status_code == 200, "Incorrect HTTP code."

    def test_get_store_inventory(self):
        response = requests.get(url=self.base_url + self.store_get_inventory_url)

        with check:
            assert response.status_code == 201, "Intentional fail."

        print("--- Soft assertions in the test ---")

        with check:
            assert response.status_code == 202, "Incorrect HTTP code."

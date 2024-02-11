import pytest

import requests

from test_ci_ct.base_test import BaseTest


class TestPets(BaseTest):
    @pytest.mark.parametrize("status", ["available", "pending", "sold"])
    @pytest.mark.pets
    def test_find_pets_by_status(self, status):
        response = requests.get(url=self.base_url + self.find_by_status_url, params={"status": status})
        assert response.status_code == 200, "Incorrect HTTP code."

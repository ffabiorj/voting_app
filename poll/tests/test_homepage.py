import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_home_status_code_200(client):
    url = reverse("home")
    response = client.get(url)
    assert response.status_code == 200
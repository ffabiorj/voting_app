import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed, assertContains


@pytest.mark.django_db
def test_home_status_code_200(client):
    url = reverse("home")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_template_used(client):
    url = reverse("home")
    response = client.get(url)
    assertTemplateUsed(response, "index.html")


@pytest.mark.django_db
def test_polls_link(client):
    url = reverse("home")
    expected = f'href="{url}"'
    response = client.get(url)
    assertContains(response, expected)


@pytest.mark.django_db
def test_create_link(client):
    url = reverse("create")
    expected = f'href="{url}"'
    response = client.get(url)
    assertContains(response, expected)

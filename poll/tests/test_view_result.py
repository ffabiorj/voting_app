import pytest
from django.urls import reverse
from poll.models import Poll


@pytest.fixture
def create_poll():
    poll = Poll.objects.create(
        question="teste",
        option_one="teste1",
        option_two="teste2",
        option_three="teste3",
    )
    yield poll


@pytest.mark.django_db
def test_result_status_code_ok(client, create_poll):
    response = client.get(reverse("result", kwargs={"pk": create_poll.id}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_result_status_code_error(client):
    response = client.get(reverse("result", kwargs={"pk": 10}))
    assert response.status_code == 404

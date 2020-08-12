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
def test_vote_status_code_OK(client, create_poll):
    response = client.get(reverse("vote", kwargs={"pk": create_poll.id}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_vote_option_one(client, create_poll):
    data = {"poll": "option1"}
    response = client.post(
        reverse("vote", kwargs={"pk": create_poll.id}), data=data, follow=True
    )
    assert response.status_code == 200


@pytest.mark.django_db
def test_vote_option_two(client, create_poll):
    data = {"poll": "option2"}
    response = client.post(
        reverse("vote", kwargs={"pk": create_poll.id}), data=data, follow=True
    )
    assert response.status_code == 200


@pytest.mark.django_db
def test_vote_option_three(client, create_poll):
    data = {"poll": "option3"}
    response = client.post(
        reverse("vote", kwargs={"pk": create_poll.id}), data=data, follow=True
    )
    assert response.status_code == 200


@pytest.mark.django_db
def test_vote_error_400(client, create_poll):
    data = {"poll": ""}
    response = client.post(
        reverse("vote", kwargs={"pk": create_poll.id}), data=data, follow=True
    )
    assert response.content.decode() == "Invalid form"
    assert response.status_code == 400


@pytest.mark.django_db
def test_vote_error_404(client):
    data = {"poll": "option1"}
    response = client.post(reverse("vote", kwargs={"pk": 10}), data=data, follow=True)
    assert response.status_code == 404

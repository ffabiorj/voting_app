import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_post_status_200(client):
    data = {
        "question": "teste",
        "option_one": "teste1",
        "option_two": "teste2",
        "option_three": "teste3",
    }
    response = client.post(reverse("create"), data=data, follow=True)
    assert response.status_code == 200

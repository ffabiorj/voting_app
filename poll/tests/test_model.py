import pytest

from django.contrib.auth.models import User


@pytest.mark.django_db
def test_user_create():
    User.objects.create_user('Fabio', 'fabio@gmail.com', '12345667')
    assert User.objects.count() == 1
import pytest
from poll.models import Poll


@pytest.mark.django_db
def test_poll_has_one_poll():
    Poll.objects.create(
        question="What is the best test for python?",
        option_one="Unittest",
        option_two="Pytest",
        option_three="Mommy",
    )
    Poll.objects.count() == 1


@pytest.mark.django_db
def test_poll_has_ten_votes():
    Poll.objects.create(
        question="What is the best test for python?",
        option_one="Unittest",
        option_two="Pytest",
        option_three="Mommy",
    )
    result = Poll.objects.first()
    result.option_one_count = 3
    result.option_two_count = 6
    result.option_three_count = 1

    assert result.total() == 10


@pytest.mark.django_db
def test_poll_str():
    Poll.objects.create(
        question="What is the best test for python?",
        option_one="Unittest",
        option_two="Pytest",
        option_three="Mommy",
    )
    expect = Poll.objects.first()
    assert expect.__str__() == "What is the best test for python?"

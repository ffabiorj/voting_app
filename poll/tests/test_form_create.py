import pytest
from poll.forms import CreatePollForm


@pytest.mark.django_db
def test_form_has_fields():
    form = CreatePollForm()
    expected = ["question", "option_one", "option_two", "option_three"]
    assert expected == list(form.fields)


@pytest.mark.django_db
def test_form_is_valid_true():
    form = CreatePollForm(
        dict(
            question="teste",
            option_one="teste1",
            option_two="teste2",
            option_three="teste3",
        )
    )
    expected = form.is_valid()
    assert expected is True


@pytest.mark.django_db
def test_validation_error_question():
    form = CreatePollForm(dict(question=""))
    expected = form.is_valid()
    assert form.errors["question"] == ["This field is required."]
    assert expected is False


@pytest.mark.django_db
def test_validation_error_option_one():
    form = CreatePollForm(dict(question="teste", option_one=""))
    expected = form.is_valid()
    assert form.errors["option_one"] == ["This field is required."]
    assert expected is False


@pytest.mark.django_db
def test_validation_error_option_two():
    form = CreatePollForm(dict(question="teste", option_one="teste1", option_two=""))
    expected = form.is_valid()
    assert form.errors["option_two"] == ["This field is required."]
    assert expected is False


@pytest.mark.django_db
def test_validation_error_option_three():
    form = CreatePollForm(
        dict(
            question="teste", option_one="teste1", option_two="teste2", option_three=""
        )
    )
    expected = form.is_valid()
    assert form.errors["option_three"] == ["This field is required."]
    assert expected is False

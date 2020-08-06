# Voting App


## Tools
* Django


## How to run locally.

1. Clone the repository.
2. Enter the folder
3. Create an enviroment with python 3.8.
4. Active the enviroment.
5. Install the dependencies.
6. run env_gen file
7. Run migrations
8. Create an user
9. Run the project
10. Access the link


```
- git clone git@github.com:ffabiorj/voting_app.git
- cd voting_app
- python3 -m venv .venv
- sourch .venv/bin/activate
- pip install -r requirements-dev.txt
- python contrib.env_gen.py
- python manage.py migrate
- python manage.py shell
  from django.contrib.auth.models import User
  user = User.objects.create_user(username=<yourname>', password='<password>')
  user.save()
- python manage.py runserver
- http://127.0.0.1:8000

```

### Run tests
```
pytest
```

### Links for tools
[Django](https://docs.djangoproject.com/)

[Codecov](https://codecov.io/)

[Travis](https://travis-ci.com/)

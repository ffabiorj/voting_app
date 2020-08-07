from django.urls import path
from poll.views import home

urlpatterns = [
    path('', home, name='home')
]

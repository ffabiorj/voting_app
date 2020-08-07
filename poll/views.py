from django.shortcuts import render
from poll.models import Poll


def home(request):
    polls = Poll.objects.all()
    context = {
        "polls": polls
    }
    return render(request, 'index.html', context)

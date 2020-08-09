from django.shortcuts import render, redirect
from poll.models import Poll
from poll.forms import CreatePollForm


def home(request):
    polls = Poll.objects.all()
    context = {"polls": polls}
    return render(request, "index.html", context)


def create(request):
    if request.method == "POST":
        form = CreatePollForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CreatePollForm()

    context = {"form": form}
    return render(request, "create.html", context)

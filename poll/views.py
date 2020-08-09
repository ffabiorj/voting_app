from django.shortcuts import render, redirect, get_object_or_404
from poll.models import Poll
from poll.forms import CreatePollForm
from django.http import HttpResponse


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

def vote(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    
    if request.method == "POST":
        selected_option = request.POST['poll']
        print(selected_option)
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option2_two_count += 1
        elif selected_option == 'option3':
            poll.option2_three_count
        else:
            return HttpResponse(400, 'Invalid form')

        poll.save()

        return redirect('home')

    context = {
        'poll': poll
    }
    return render(request, 'vote.html', context)

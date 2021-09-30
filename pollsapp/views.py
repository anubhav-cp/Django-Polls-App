from django.shortcuts import redirect, render
from .models import Poll
from django.http import HttpResponse
from .forms import createPollForm

def homePage(request):
    polls = Poll.objects.all()

    context = {'polls': polls}
    return render(request, 'pollsapp/homePage.html', context)



def createPoll(request):
    form = createPollForm()

    if request.method == 'POST':
        form = createPollForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('home')
            
    context = {'form': form}
    return render(request, 'pollsapp/createPoll.html', context)



def pollResult(request, pk):
    poll = Poll.objects.get(id=pk)

    context = {'poll': poll}
    return render(request, 'pollsapp/pollResult.html', context)


def votePoll(request, pk):
    polls = Poll.objects.get(id=pk)

    if request.method == 'POST':
        selected_option = request.POST['poll']

        if selected_option == 'option_1':
            polls.option_1_count += 1

        elif selected_option == 'option_2':
            polls.option_2_count += 1

        elif selected_option == 'option_3':
            polls.option_3_count += 1

        elif selected_option == 'option_4':
            polls.option_4_count += 1

        else:
            return HttpResponse(400, 'Invalid form option')

        polls.save()

        return redirect('home')



    context = {'polls': polls}
    return render(request, 'pollsapp/vote.html', context)
from django.shortcuts import render,get_object_or_404,redirect
from django.template import loader
from django.http import JsonResponse
from django.db.models import Sum
from django.contrib import messages

from .models import Poll,Choice
from .forms import VoteForm

def index(request):
  latest_polls=Poll.objects.order_by('-pub_date')[:5]
  context={'latest_polls':latest_polls}
  return render(request,'index.html',context)

def detail(request, poll_id):
  try:
    poll =  Poll.objects.get(pk=poll_id)
    total_votes = poll.choice_set.aggregate(Sum('votes'))['votes__sum']
  except Poll.DoesNotExist:
    messages.error(request, "Poll not found.")
    return redirect('Polling:index')
  
  form = VoteForm(poll_id)

  if request.method == 'POST':
    form = VoteForm(poll_id, request.POST)
    if form.is_valid():
      choice_id = form.cleaned_data['choice'].id
      choice=get_object_or_404(Choice, pk=choice_id)
      choice.votes += 1
      choice.save()
      messages.success(request, "Thank you for voting!")
      return redirect('polling:detail', poll_id=poll_id)
  
  context = {'poll':poll, 'total_votes':total_votes, 'form':form}

  return render(request,'detail.html', context)


def poll_results_api(request, poll_id):
  poll = get_object_or_404(Poll, pk=poll_id)
  total_votes = poll.choice_set.aggregate(Sum('votes'))['votes__sum']
  results = [{'choice_text':choice.choice_text, 'votes':choice.votes} for choice in poll.choice_set.all()]
  return JsonResponse({'results':results, 'total_votes':total_votes})



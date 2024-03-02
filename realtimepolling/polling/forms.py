from django import forms
from .models import Choice
from django.shortcuts import render,redirect
from django.db.models import Sum
from django.contrib import messages

from .models import Poll, Choice


class VoteForm(forms.ModelForm):
  class Meta:
    model = Choice
    fields = ['choice']
  choice=forms.ModelChoiceField(queryset=None)

  def __init__(self, poll_id , *args, **kwargs):
    super(VoteForm, self).__init__(*args,**kwargs)
    self.fields['choice'].queryset = Choice.objects.filter(poll_id=poll_id)


  


 
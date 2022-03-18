from pipes import Template
from ssl import cert_time_to_seconds
from urllib.request import Request
from django.shortcuts import render, redirect
from django.http import HttpResponse, response
from django.views.generic import CreateView
from registration_form import forms
# Create your views here.


from .models import Person

def home(request):
    form = forms.create_person_form()

    if request.method == 'POST':
        form = forms.create_person_form(request.POST)
        #print(form.cleaned_data['Name'])
        if form.is_valid():
            form.save()
            return redirect('success')
    
    context = {
        'form': form
    }
    return render(request, "registration_form/person_form.html", context)

def succ(request):
    context={}
    return render(request, "registration_form/success.html", context)

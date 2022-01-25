from pipes import Template
from urllib.request import Request
from django.shortcuts import render
from django.http import HttpResponse, response
from django.views.generic import CreateView
# Create your views here.


from .models import Person

class PersonCreateView(CreateView):
    model = Person
    fields = ('name', 'email', 'branch', 'year', 'query')

def succ(request):
    context={}
    return render(request, "registration_form/success.html", context)

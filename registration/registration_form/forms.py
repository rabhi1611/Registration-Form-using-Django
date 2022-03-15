from dataclasses import field, fields
from django.forms import ModelForm
from registration_form import models

class create_person_form(ModelForm):
    class Meta:
        model = models.Person
        fields = "__all__"
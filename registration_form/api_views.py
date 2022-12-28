from rest_framework.generics import ListAPIView

from registration_form.serializers import PersonSerializer
from registration_form.models import Person

from rest_framework.filters import SearchFilter

from django_filters.rest_framework import DjangoFilterBackend

class ProductList(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['id']
    search_fields = ['name']

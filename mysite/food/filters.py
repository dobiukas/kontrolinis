import django_filters
from .models import *

class fooditemFilter(django_filters.FilterSet):
    class Meta:
        model = Food
        fields = ['name']
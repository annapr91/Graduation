from distutils.util import strtobool

import django_filters
# from .models import *
from account.models import Kindergarden,KIDCHOICE
from django.forms import CheckboxSelectMultiple
from django_filters import ModelChoiceFilter, ChoiceFilter, ModelMultipleChoiceFilter, filters

BOOLEAN_CHOICES = (('false', 'False'), ('true', 'True'),)


class KindFilter(django_filters.FilterSet):
    name = django_filters.ModelChoiceFilter(queryset=Kindergarden.objects.all())
    addition = django_filters.ModelMultipleChoiceFilter(queryset=KIDCHOICE.objects.all(),widget=CheckboxSelectMultiple )
    rayon = django_filters.CharFilter(label='rayon')
    class Meta:
        model = Kindergarden
        fields = ['name', 'rayon','addition']

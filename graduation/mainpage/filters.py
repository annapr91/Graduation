from distutils.util import strtobool

import django_filters
# from .models import *
from account.models import Kindergarden,KIDCHOICE
from django.utils.translation import gettext_lazy as _
from django.forms import CheckboxSelectMultiple
from django_filters import ModelChoiceFilter, ChoiceFilter, filters, ModelMultipleChoiceFilter


# BOOLEAN_CHOICES = (('false', 'False'), ('true', 'True'),)


class KindFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(label = _('Имя'),field_name="translations__name",lookup_expr='icontains')
    translations__addition = django_filters.ModelChoiceFilter(label = _('Дополнительные кружки'),field_name='translations__addition',
                                                                      queryset=KIDCHOICE.objects.all())
    # area = django_filters.ModelChoiceFilter(queryset=Kindergarden.objects.all())

    # area = django_filters.ModelChoiceFilter(field_name = 'area',queryset=Kindergarden.objects.all())
    class Meta:
        model = Kindergarden
        fields = ['name','translations__addition','area','free_places']

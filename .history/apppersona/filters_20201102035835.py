import django_filters
from django_filters import CharFilter

from .models import *

class OrderFilter(django_filters.FilterSet):
	
	nombre = CharFilter(field_name='nombre', lookup_expr='icontains')


	
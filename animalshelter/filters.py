import django_filters
from .models import Animal

class AnimalFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label='Name contains')

    class Meta:
        model = Animal  
        fields = ['name', 'breed', 'color','temper','size','sex']  

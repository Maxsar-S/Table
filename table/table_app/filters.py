from django_filters import rest_framework as filters
from table_app.models import Cell


class CellFilter(filters.FilterSet):
    class Meta:
        model = Cell
        fields = {
            'date': ['lt', 'gt', 'exact', 'contains'],
            'name': ['lt', 'gt', 'exact', 'contains'],
            'quantity': ['lt', 'gt', 'exact', 'contains'],
            'distance': ['lt', 'gt', 'exact', 'contains'],
        }

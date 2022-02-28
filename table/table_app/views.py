from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny
from .serializers import CellSerializer
from .models import Cell
from .filters import CellFilter
from .pagination import LimitOffsetPaginationByTwenty


class CellList(generics.ListAPIView):
    queryset = Cell.objects.all().order_by('name')
    serializer_class = CellSerializer
    permission_classes = [AllowAny]
    pagination_class = LimitOffsetPaginationByTwenty

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ('name', 'quantity', 'distance')
    filterset_class = CellFilter

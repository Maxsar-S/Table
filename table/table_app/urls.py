from django.urls import path
from . import views

urlpatterns = [
    path('api/table/', views.CellList.as_view()),
]

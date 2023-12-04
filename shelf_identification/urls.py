# shelf_identification/urls.py
from django.urls import path
from .views import identify_shelf_shapes
from shelf_identification import views
from . import views

urlpatterns = [
    path('identify-shelf-shapes/', views.identify_shelf_shapes, name='identify_shelf_shapes'),
]

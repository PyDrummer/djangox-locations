from django.urls import path
from .views import LocationListView, LocationDetailView, LocationCreateView, LocationDeleteView, LocationUpdateView

urlpatterns = [
    path('', LocationListView.as_view(), name='locations_list'),
    path('<int:pk>/', LocationDetailView.as_view(), name='locations_details'),
    path('new/', LocationCreateView.as_view(), name='locations_create'),
    path('<int:pk>/edit', LocationUpdateView.as_view(), name='locations_update'),
    path('<int:pk>/delete', LocationDeleteView.as_view(), name='locations_delete'),
]

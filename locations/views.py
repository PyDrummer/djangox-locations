from django.shortcuts import render

# Create your views here.
from django.db import models
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Location

class LocationListView(ListView):
  template_name = "locations/locations-list.html"
  model = Location

class LocationCreateView(CreateView):
  template_name = "locations/locations-create.html"
  model = Location
  fields = ['location', 'description', 'name']
  

class LocationDetailView(DetailView):
  template_name = "locations/locations-detail.html"
  model = Location

class LocationUpdateView(UpdateView):
  template_name = "locations/locations-update.html"
  model = Location
  fields = ['location', 'description', 'name']

class LocationDeleteView(DeleteView):
  template_name = "locations/locations-delete.html"
  model = Location
  success_url = reverse_lazy("locations_list")

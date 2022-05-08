from django.shortcuts import render
from django.views.generic import ListView
from rentals.models import Equipment

class EquipmentListView(ListView):
    model = Equipment
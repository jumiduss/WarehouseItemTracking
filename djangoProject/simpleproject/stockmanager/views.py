from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from stockmanager.models import Location,Item

class ItemView(generic.DetailView):
    model = Item
    template_name = "stockmanager/item.html"
    context_object_name = "item"
    

class ItemIndexView(generic.ListView):
    model = Item
    context_object_name = "item_set"
    template_name = "stockmanager/item_index.html"

    def get_queryset(self):
        return Item.objects.all()
    

class LocationView(generic.DetailView):
    model = Location
    template_name = "stockmanager/location.html"
    context_object_name = "location"

class LocationIndexView(generic.ListView):
    model = Location
    context_object_name = "location_set"
    template_name = "stockmanager/location_index.html"

    def get_queryset(self):
        return Location.objects.all()
    


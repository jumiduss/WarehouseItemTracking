from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from stockmanager.models import Location,Item

class ItemIndexView(generic.ListView):
    template_name = "stockmanager/item_index.html"
    context_object_name = "item_set"

    def get_queryset(self):
        return Item.objects.order_by("item_name")

class ShelfIndexView(generic.ListView):
    template_name = "stockmanager/shelf_index.html"
    context_object_name = "shelf_set"

    def get_queryset(self):
        return Location.objects.order_by("f_num","m_num","l_num",)

class ShelfView(generic.DetailView):
    model = Location
    context_object_name = "location_list"
    
class ItemView(generic.DetailView):
    model = Item
    context_object_name = "item_list"


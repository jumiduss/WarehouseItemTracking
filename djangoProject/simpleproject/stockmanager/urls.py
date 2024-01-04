from django.urls import path,include
from . import views

app_name = 'stockmanager'

urlpatterns = [
    path("item_index/", views.ItemIndexView.as_view(), name="item_index"),
    path("item_index/<int:pk>", views.ItemView.as_view(), name='item'),
    path("location_index/", views.LocationIndexView.as_view(), name="location_index"),
    path("location_index/<int:pk>", views.LocationView.as_view(), name='location'),
]
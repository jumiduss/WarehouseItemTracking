from django.urls import path,include
from . import views

app_name = 'stockmanager'

urlpatterns = [
    path("",                  views.IndexView.as_view, name="index"   ),
    path("location/<int:pk>", views.ShelfView.as_view, name='location'),
    path("item/<int:pk>",     views.ItemView.as_view,  name='item'    ),
]
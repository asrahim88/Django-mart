from django.urls import path
from . import views

urlpatterns = [
    path("complete_order/", views.oder_complete, name= 'complete_order'),
    path("place_order/", views.placeOrder, name= 'place_order'),
]

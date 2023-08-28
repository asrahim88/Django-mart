from django.urls import path
from . import views

urlpatterns = [
    path("store/", views.store, name= 'store'),
    path("product_details/", views.product_details, name= 'product_details'),
]

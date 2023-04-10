from django.urls import path
from . import views


urlpatterns=[
    path('getListings', views.getListings, name="jsondata")
]
from django.urls import path
from . import views
from .views import delete_property
from .views import update_listing

urlpatterns=[
    path('getListings', views.getListings, name="jsondata"),
    path('getCities', views.getCities, name="jsondata"),
    path('addListings', views.addListings, name="jsondata"),
    path('property/<int:listing_id>/', delete_property, name='delete_property'),
    path('listings/update/<int:listing_id>/', update_listing, name='update_listing'),


]
from django.urls import path
from . import views
from .views import delete_property

urlpatterns=[
    path('getListings', views.getListings, name="jsondata"),
    path('getCities', views.getCities, name="jsondata"),
    path('updateListings', views.updateListings, name="jsondata"),
    path('property/<int:listing_id>/', delete_property, name='delete_property'),

]
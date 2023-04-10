from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Listings


# Create your views here.
def getListings(request):
    listings = list(Listings.objects.all().values())
    return JsonResponse(listings, safe=False)

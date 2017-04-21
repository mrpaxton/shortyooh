from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from .models import ShortURL

def test_view(request, *args, **kwargs):
    return HttpResponse("Dummy page here.")

def home_view_fbv(request, *args, **kwargs):
    #fbv way to access the POST data
    if request.method == "POST":
        print(request.POST)
    return render(request, "shorterner/home.html", {})

def shorturl_redirect_view(request, shortcode=None, *args, **kwargs):
    obj = get_object_or_404(ShortURL, shortcode=shortcode)
    print("Found {su}.".format(su=obj.url))
    return HttpResponseRedirect(obj.url)

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "shorterner/home.html", {})

    def post(self, request, *args, **kwargs):
        #could access the input data like below, but better use Form
        #that will help with validation and give clean inputs
        print(request.POST)
        print(request.POST.get("url"))
        return render(request, "shorterner/home.html", {})

class ShorturlCBView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(ShortURL, shortcode=shortcode)
        print("Found {su}.".format(su=obj.url))
        return HttpResponseRedirect(obj.url)

"""
    Objective: try to get object using incoming shortcode
    Simple but not the best way is below using try-catch
    try:
        obj = ShortURL.objects.get(shortcode=shortcode)
    except:
        obj = ShortURL.objects.all().first()

    Better way is below
    obj_url = None
    qs = ShortURL.objects.filter(shortcode__iexact=shortcode.upper())
    if qs.exists() and qs.count() == 1:
        obj = qs.first()
        obj_url = obj.url
    return HttpResponse("Hello {sc}.".format(sc=obj_url or "there!"))

    Best way is using the get_object_or_404() method
"""

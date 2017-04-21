from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from .models import ShortURL
from .forms import SubmitURLForm


class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = SubmitURLForm()
        context = {
            'title': "Shortyooh.com helps you shortern URLs",
            'form': the_form,
        }
        return render(request, "shorterner/home.html", context)

    def post(self, request, *args, **kwargs):
        #create a form object using the request.POST
        the_form = SubmitURLForm(request.POST)
        if the_form.is_valid():
            print(the_form.cleaned_data)
        #put the form object into context
        context = {
            'title': "Shortyooh.com helps you shortern URLs",
            'form': the_form,
        }
        #now the keys of the context are accessible in the template
        return render(request, "shorterner/home.html", context)

class ShorturlCBView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(ShortURL, shortcode=shortcode)
        print("Found {su}.".format(su=obj.url))
        return HttpResponseRedirect(obj.url)

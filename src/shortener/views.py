from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from .models import ShortURL
from .forms import SubmitURLForm


class HomeView(View):
    context = {
        'title': "Shortyooh.com helps you shortern URLs",
        'form': None,
    }

    def get(self, request, *args, **kwargs):
        get_form = SubmitURLForm()
        context = self.context
        context['form'] = get_form
        return render(request, "shortener/home.html", context)

    def post(self, request, *args, **kwargs):
        #create a form object using the request.POST
        post_form = SubmitURLForm(request.POST)

        #put the form object into context
        context = self.context
        context['form'] = post_form
        template = "shortener/home.html"

        if post_form.is_valid():
            print(post_form.cleaned_data.get("url"))
            new_url = "http://" + post_form.cleaned_data.get("url")
            obj, created = ShortURL.objects.get_or_create(url=new_url)
            context = {
                'object': obj,
                'created': created,
            }
            template = "shortener/success.html" if created \
                    else "shortener/already-exists.html"

        #now the keys of the context are accessible in the template
        return render(request, template, context)

class ShorturlCBView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(ShortURL, shortcode=shortcode)
        print("Found {su}.".format(su=obj.url))
        return HttpResponseRedirect(obj.url)

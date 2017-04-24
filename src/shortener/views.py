from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import View

from analytics.models import ClickEvent
from .models import ShortURL
from .forms import SubmitURLForm


class HomeView(View):

    context = {
        'title': "Let's shorten some URLs",
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



class URLRedirectView(View):


    def get(self, request, shortcode=None, *args, **kwargs):
        qs = ShortURL.objects.filter(shortcode__iexact=shortcode)
        short_urls = list(qs)
        if not short_urls or len(short_urls) != 1:
            raise Http404
        obj = short_urls[0]
        ClickEvent.objects.create_event(obj)
        return HttpResponseRedirect(obj.url)


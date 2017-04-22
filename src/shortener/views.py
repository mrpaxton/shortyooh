from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import View

from analytics.models import ClickEvent
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



class URLRedirectView(View):


    def get(self, request, shortcode=None, *args, **kwargs):
        qs = ShortURL.objects.filter(shortcode__iexact=shortcode)
        if qs.count() != 1 and not qs.exists():
            raise Http404
        obj = qs.first()
        print(ClickEvent.objects.create_event(obj))
        return HttpResponseRedirect(obj.url)


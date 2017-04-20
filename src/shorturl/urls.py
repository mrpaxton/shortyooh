"""shorturl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from shorterner.views import shorturl_redirect_view, ShorturlCBView

urlpatterns = [
    url(r'^suadmin/', admin.site.urls),
    url(r'^fbv/(?P<shortcode>\w{6,15})/$', shorturl_redirect_view),
    url(r'^cbv/(?P<shortcode>\w{6,15})/$', ShorturlCBView.as_view()),
]

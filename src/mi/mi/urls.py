from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name="base.html"), name='index'),
    # url(r'^mi/', include('mi.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

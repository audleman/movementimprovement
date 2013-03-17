from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
import backbone


admin.autodiscover()
backbone.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    # Examples:
    url(r'^$', TemplateView.as_view(template_name="dashboard.html"), name='index'),
    # url(r'^mi/', include('mi.foo.urls')),
    (r'^backbone/', include(backbone.site.urls)),

)

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'daily_log.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^log/', include('weight.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

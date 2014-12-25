from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web_portal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.urls')),
)

# include urls from packages
urlpatterns += patterns('',
    (r"^", include("web_portal.core.main.urls")),
)
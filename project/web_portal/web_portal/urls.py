from django.conf.urls import patterns, include
from django.contrib import admin

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r"^", include("web_portal.core.main.urls")),
    (r"^", include("web_portal.core.users.urls")),
    (r"^", include("web_portal.core.courses.urls")),
)
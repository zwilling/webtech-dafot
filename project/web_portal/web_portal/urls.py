from django.conf.urls import patterns, include
from django.contrib import admin
from django.conf import settings

# handler400 = 'web_portal.core.errors.views.bad_request'
# handler403 = 'web_portal.core.errors.views.permission_denied'
handler404 = 'web_portal.core.errors.views.page_not_found'
# handler500 = 'web_portal.core.errors.views.server_error'

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r"^", include("web_portal.core.main.urls")),
    (r"^", include("web_portal.core.users.urls")),
    (r"^", include("web_portal.core.courses.urls")),
)
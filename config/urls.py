from django.conf import settings

from django.contrib import admin
from django.urls import path, include

from apps.core.views import IndexView


urlpatterns = [
    path(
        "",
        IndexView.as_view(),
        name="index",
    ),
    path(
        "users/",
        include("apps.users.urls"),
    ),
]

urlpatterns += (
        path(
            "admin/",
            admin.site.urls,
        ),
    )

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

"""
URL configuration for admin_panel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import RedirectView

from panel import views as panel_views

admin.site.site_header = "Webmail Administration"
admin.site.site_title = "Webmail Administration Portal"
admin.site.index_title = ""
admin.site.site_url = ""

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("", RedirectView.as_view(url="admin/", permanent=False)),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)

if settings.ROUNDCUBE_ENABLE:
    urlpatterns = [
        path(
            "roundcube/",
            include([re_path(r"(?P<path>.*)", panel_views.RoundcubeProxy.as_view())]),
        )
    ] + urlpatterns

if "debug_toolbar" in settings.INSTALLED_APPS:
    urlpatterns = [path("__debug__/", include("debug_toolbar.urls"))] + urlpatterns

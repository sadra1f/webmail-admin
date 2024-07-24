from django.conf import settings
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from revproxy.views import ProxyView


class RoundcubeProxy(UserPassesTestMixin, ProxyView):
    upstream = settings.ROUNDCUBE_URL

    def test_func(self):
        current_user = self.request.user
        return (
            settings.ROUNDCUBE_ENABLE
            and settings.ROUNDCUBE_URL
            and current_user.is_authenticated
            and (current_user.is_superuser or current_user.is_staff)
        )

    def handle_no_permission(self):
        raise PermissionDenied()

    def dispatch(self, *args, **kwargs):
        response = super(RoundcubeProxy, self).dispatch(*args, **kwargs)
        response["X-Frame-Options"] = "SAMEORIGIN"
        return response

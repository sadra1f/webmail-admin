# from django.shortcuts import render
from revproxy.views import ProxyView


# TODO: Complete and use the proxy view
class RoundcubeProxy(ProxyView):
    upstream = "http://roundcube"
    # upstream = "http://127.0.0.1:80"

    def dispatch(self, *args, **kwargs):
        response = super(RoundcubeProxy, self).dispatch(*args, **kwargs)
        response["X-Frame-Options"] = "SAMEORIGIN"
        return response

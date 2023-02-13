import os


class ServerURLWithPortHackMiddlware(object):
    """
    A way to set HTTP_HOST to HTTP_HOST + (a port number).
    This is usefull when you want to run Django on your local computer as a
    developer server. Example in Docker.
    Django doesn't know which PORT you are using all the way to the browser,
    so if you don't fix this, reverse URLs will be all wrong..
    """

    def process_request(self, request):
        if os.environ.get('HTTP_PORT', None) and request.META.get('HTTP_HOST', None):
            request.META[
                'HTTP_HOST'
            ] = f"{request.META['HTTP_HOST']}:{os.environ['HTTP_PORT']}"

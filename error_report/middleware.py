from __future__ import absolute_import, unicode_literals

from error_report import log_error


class ExceptionProcessor(object):
    """
    Middleware that save details of exception that occurs in any app to the database.
    """

    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        log_error(request=request)

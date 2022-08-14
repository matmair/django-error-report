from __future__ import absolute_import, unicode_literals

import traceback
import sys

from django.views.debug import ExceptionReporter

from error_report.models import Error
from error_report.settings import ERROR_DETAIL_SETTINGS


def log_error(request):
    """Log an error to the database.

    - Uses python exception handling to extract error details

    Arguments:
        request: Request object of the raising party
    """

    kind, info, data = sys.exc_info()

    if not ERROR_DETAIL_SETTINGS.get('ERROR_DETAIL_ENABLE', True):
        return None

    error = Error.objects.create(
        kind=kind.__name__,
        html=ExceptionReporter(request, kind, info, data).get_traceback_html(),
        path=request.build_absolute_uri(),
        info=info,
        data='\n'.join(traceback.format_exception(kind, info, data)),
    )
    error.save()

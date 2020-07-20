from future import standard_library
standard_library.install_aliases()
from django.shortcuts import redirect
from django.views.static import serve

import os.path
from urllib.parse import urlparse


def sendfile(request, filename, **kwargs):
    '''
    Send file using django dev static file server.

    DO NOT USE IN PRODUCTION
    this is only to be used when developing and is provided
    for convenience only
    '''
    parseresult = urlparse(filename)
    if parseresult.scheme:
        return redirect(filename)

    dirname = os.path.dirname(filename)
    basename = os.path.basename(filename)
    return serve(request, basename, dirname)

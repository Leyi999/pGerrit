from functools import wraps
import requests
from types import SimpleNamespace
from Gerrit.utils import urljoin


class GerritRest(object):
    """
    docstring for RestAPI
    """
    def get(func):
        @wraps(func)
        def decorator_get(self, *args, **kwargs):
            url = func(self)
            self.session.headers["Accept"] = "application/json"
            res = self.session.get(url, verify=self.kwargs["verify"], params=kwargs)
            res._content = res._content.replace(b")]}'\n", b"")
            # des.resultType
            return res.json(object_hook=lambda d: SimpleNamespace(**d))
        return decorator_get

    def put(func):
        @wraps(func)
        def decorator_get(self, payload, headers=None, **kwargs):
            url = func(self, payload, headers=headers)
            self.session.headers["Accept"] = "application/json"
            res = self.session.put(url, payload, headers=headers, verify=self.kwargs["verify"], params=kwargs)
            # res._content = res._content.replace(b")]}'\n", b"")
            # des.resultType
            return res
        return decorator_get

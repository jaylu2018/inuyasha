import httpx


class BaseRequest:

    @staticmethod
    def get(url, params=None, **kwargs):
        return httpx.get(url, params=params, **kwargs)

    @staticmethod
    def post(url, data=None, **kwargs):
        return httpx.post(url, data=data, **kwargs)

    @staticmethod
    def put(url, data=None, **kwargs):
        return httpx.put(url, data=data, **kwargs)

    @staticmethod
    def delete(url, **kwargs):
        return httpx.delete(url, **kwargs)

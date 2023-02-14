import requests


class BaseRequest:

    @staticmethod
    def get(url, params=None, **kwargs):
        return requests.get(url, params=params, **kwargs)

    @staticmethod
    def post(url, data=None, **kwargs):
        return requests.post(url, data=data, **kwargs)

    @staticmethod
    def put(url, data=None, **kwargs):
        return requests.put(url, data=data, **kwargs)

    @staticmethod
    def delete(url, **kwargs):
        return requests.delete(url, **kwargs)

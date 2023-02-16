import json

from pytest_cases import parametrize_with_cases

from inuyasha import TestCase, log
from ..test_data.busi import BusiAPIData


class TestBusiAPISample(TestCase):

    @parametrize_with_cases('param', cases=BusiAPIData, prefix="busi_")
    def test_busi_api_case_get(self, param):
        log.info(param)
        response = self.requests.get("https://httpbin.org/get")
        log.info(response.text)
        log.info(response.request.content.decode())

    @parametrize_with_cases('param', cases=BusiAPIData, prefix="busi_")
    def test_busi_api_case_post(self, param):
        log.info(param)
        response = self.requests.post('https://httpbin.org/post', data=json.dumps(param))
        log.info(response.text)
        log.info(json.loads(response.request.content.decode()))

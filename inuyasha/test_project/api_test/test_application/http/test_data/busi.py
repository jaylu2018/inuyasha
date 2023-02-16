from pytest_cases import parametrize


class BusiAPIData:
    @parametrize(data=(
            {"api接口测试": {"userName": 'luyh'}},
    ))
    def busi_api_test(self, data):
        template = {
            "userName": list(data.values())[0]["userName"],
        }
        template.update(list(data.values())[0])
        return template

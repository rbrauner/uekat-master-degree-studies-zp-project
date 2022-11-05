from fastapi.testclient import TestClient
from src.app.app import app


class TestPrime:
    client = TestClient(app)

    def test_valid_numbers(self):
        testData = [
            {"request": {"url": "/prime/-2"}, "response": {"status_code": 200,
                                                           "data": {"is_prime": False, "number": -2}}},
            {"request": {"url": "/prime/-1"}, "response": {"status_code": 200,
                                                           "data": {"is_prime": False, "number": -1}}},
            {"request": {"url": "/prime/0"}, "response": {"status_code": 200,
                                                          "data": {"is_prime": False, "number": 0}}},
            {"request": {"url": "/prime/1"}, "response": {"status_code": 200,
                                                          "data": {"is_prime": False, "number": 1}}},
            {"request": {"url": "/prime/2"}, "response": {"status_code": 200,
                                                          "data": {"is_prime": True, "number": 2}}},
            {"request": {"url": "/prime/3"}, "response": {"status_code": 200,
                                                          "data": {"is_prime": True, "number": 3}}},
            {"request": {"url": "/prime/4"}, "response": {"status_code": 200,
                                                          "data": {"is_prime": False, "number": 4}}},
            {"request": {"url": "/prime/531137992816767098689588206552468627329593117727031923199444138200403559860852242739162502265229285668889329486246501015346579337652707239409519978766587351943831270835393219031728127"}, "response": {"status_code": 200,
                                                                                                                                                                                                                                                "data": {"is_prime": True, "number": 531137992816767098689588206552468627329593117727031923199444138200403559860852242739162502265229285668889329486246501015346579337652707239409519978766587351943831270835393219031728127}}},
        ]

        for td in testData:
            resp = self.client.get(td['request']['url'])
            assert resp.status_code == td['response']['status_code']
            assert resp.json() == td['response']['data']

    def test_invalid_numbers(self):
        testData = [
            {"request": {"url": "/prime/"},
                "response": {"status_code": 404, "data": {"detail": "Not Found"}}},
            {"request": {"url": "/prime/ "}, "response": {"status_code": 422, "data": {"detail": [
                {"loc": ["path", "number"], "msg":"value is not a valid integer", "type":"type_error.integer"}]}}},
            {"request": {"url": "/prime/_"}, "response": {"status_code": 422, "data": {"detail": [
                {"loc": ["path", "number"], "msg":"value is not a valid integer", "type":"type_error.integer"}]}}},
            {"request": {"url": "/prime/-"}, "response": {"status_code": 422, "data": {"detail": [
                {"loc": ["path", "number"], "msg":"value is not a valid integer", "type":"type_error.integer"}]}}},
            {"request": {"url": "/prime//"},
                "response": {"status_code": 404, "data": {"detail": "Not Found"}}},
        ]

        for td in testData:
            resp = self.client.get(td['request']['url'])
            assert resp.status_code == td['response']['status_code']
            assert resp.json() == td['response']['data']

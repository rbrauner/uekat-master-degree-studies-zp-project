from locust import HttpUser, task
import os

class Locust(HttpUser):
    @task
    def prime_number(self):
        self.client.get("/prime/-2")
        self.client.get("/prime/-1")
        self.client.get("/prime/0")
        self.client.get("/prime/1")
        self.client.get("/prime/2")
        self.client.get("/prime/3")
        self.client.get("/prime/4")
        self.client.get("/prime/531137992816767098689588206552468627329593117727031923199444138200403559860852242739162502265229285668889329486246501015346579337652707239409519978766587351943831270835393219031728127")

    @task
    def pricture_invert(self):
        self.client.post("/picture/invert", files={
            'file': ("test.jpg", open("data/img/test.jpg", 'rb'), 'image/jpeg')
        })

    @task
    def current_time(self):
        username = "test"
        password = "zaq1@WSX"

        response = self.client.post("/token",
            data={
                'username': username,
                'password': password,
            },
            headers={
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        )

        token = response.json()['access_token']

        self.client.get("/current-time",
            headers={
                'Authorization': 'Bearer ' + token
            }
        )



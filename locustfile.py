from locust import HttpUser, task

class TesUser(HttpUser):
    @task
    def hello(self):
        self.client.get("/")
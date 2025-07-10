from locust import HttpUser, task

class MeuTeste(HttpUser):
    @task
    def exemplo(self):
        self.client.get("/")

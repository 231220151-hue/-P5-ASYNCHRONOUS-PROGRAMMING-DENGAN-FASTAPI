from locust import HttpUser, task, between

class APIUser(HttpUser):
    wait_time = between(1, 2)

    @task(3)
    def halaman_utama(self):
        self.client.get("/")

    @task(2)
    def endpoint_async(self):
        self.client.get("/async")

    @task(1)
    def endpoint_sync(self):
        self.client.get("/sync")
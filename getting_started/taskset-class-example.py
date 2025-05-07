from locust import task, HttpUser, constant, TaskSet

class tarefas(TaskSet):
    @task
    def status_200(self):
        res = self.client.get("/200")
        print("Got status 200")
        self.interrupt(reschedule=False)
    
    @task
    def status_400(self):
        res = self.client.get("/400")
        print("Got status 400")
        self.interrupt(reschedule=False)


class usuario(HttpUser):
    host = "https://http.cat"
    wait_time = constant(2)
    tasks = [tarefas]
    
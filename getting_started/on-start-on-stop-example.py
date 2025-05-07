from locust import SequentialTaskSet, task, HttpUser, constant

class tarefas(SequentialTaskSet):
    def on_start(self):
        self.client.get("/")
        print("Indo para a home")
        
    @task
    def go_to_smartphones(self):
        self.client.get("/api/io/login")
        print("Indo para login")
    
    def on_stop(self):
        self.client.get("/")
        print("Voltando para a home")
        
class test(HttpUser):
    wait_time = constant(2)
    host = "https://www.americanas.com.br"
    tasks = [tarefas]
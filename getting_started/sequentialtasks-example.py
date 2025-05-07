from locust import task, SequentialTaskSet, HttpUser, constant, tag

class TarefasSequenciais(SequentialTaskSet):
    @tag('status_200')
    @task
    def status_200(self):
        self.client.get("/200")
        print("200")
    
    @tag('status_300')
    @task
    def status_300(self):
        self.client.get("/300")
        print("300")
        
    @tag('status_400')
    @task
    def status_400(self):
        self.client.get("/400")
        print("400")

class Teste(HttpUser):
    host = "https://http.cat"
    wait_time = constant(2)
    tasks = [TarefasSequenciais]
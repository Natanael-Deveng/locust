from locust import User, task, constant, TaskSet

class tarefa1(TaskSet):
    @task
    def task1(self):
        print("task1111")
        
class tarefa2(TaskSet):
    @task
    def task2(self):
        print("task2222")

class usuario(User):
    wait_time = constant(3)
    tasks = {tarefa1: 1, tarefa2: 3}
    
    
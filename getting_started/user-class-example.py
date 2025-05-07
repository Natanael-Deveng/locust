from locust import User, task, constant

class firstTest(User):
    weight = 2
    wait_time = constant(2)
    
    @task
    def task1(self):
        print("task1111")
        
    @task
    def task2(self):
        print("task2222")
        
class secondTest(User):
    weight = 2
    wait_time = constant(2)
    
    @task
    def task3(self):
        print("task3333")
        
    @task
    def task4(self):
        print("task4444")
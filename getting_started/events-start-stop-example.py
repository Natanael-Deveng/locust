from locust import User, task, constant, events

@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    print("A new test is starting")
    # Voce pode definir alguma variavel ou configuracao para o teste.
    
@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    print("The test finished")

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
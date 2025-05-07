from locust import User, task, constant, tag

class firstTest(User):
    wait_time = constant(2)
    
    @tag('task1')
    @task
    def task1(self):
        print("task1111")
    
    @tag('task2')    
    @task
    def task2(self):
        print("task2222")
        
# Ao rodar 'locust -f tag-decorator.py --tags task2', apenas a task2 será executada.

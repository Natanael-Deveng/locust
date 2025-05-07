from locust import HttpUser, task, constant
import time
import logging

class user1(HttpUser):
    host = "https://reqres.in"
    weight = 1
    wait_time = constant(2)
    
    @task
    def list_users(self):
        res = self.client.get("/api/users/2")
        print(res.text)
        print(res.status_code)
        print(res.headers)
        
    @task
    def create_user(self):
        res = self.client.post("/api/users",
            json={"name": "morpheus","job": "leader"}, 
            headers={"x-api-key": "reqres-free-v1"}
        )
        print(res.text)
        print(res.status_code)
        print(res.headers)
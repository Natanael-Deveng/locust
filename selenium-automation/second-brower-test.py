from locust import User, task, events, constant, SequentialTaskSet
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
 

class tarefas(SequentialTaskSet):
    def on_start(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--window-size=1920,1080')
        self.driver = webdriver.Chrome(options=options) 
        
    @task
    def home_page(self):
        start_time = time.time()
        try:
            self.driver.get("https://www.americanas.com.br")
            print("Foi pra home")
            total_time = int((time.time() - start_time) * 1000)  # em ms
            events.request.fire(
                request_type="SELENIUM",
                name="home_page",
                response_time=total_time,
                response_length=0,
                exception=None
            )
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            events.request.fire(
                request_type="SELENIUM",
                name="home_page",
                response_time=total_time,
                response_length=0,
                exception=e
            )
        
    @task
    def go_to_celulares(self):
        start_time = time.time()
        try:
            print("Entrou no go_to_celulares")
            href = '/especial/oferta-do-dia?chave=prf_hm_0_tt_7_'
            oferta_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//a[@data-testid="fs-link" and @href="{href}"]')))
            oferta_btn.click()
            print("Chegou na oferta do dia")    
            total_time = int((time.time() - start_time) * 1000)  # em ms
            events.request.fire(
                request_type="SELENIUM",
                name="go_to_celulares",
                response_time=total_time,
                response_length=0,
                exception=None
            )
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            events.request.fire(
                request_type="SELENIUM",
                name="go_to_celulares",
                response_time=total_time,
                response_length=0,
                exception=e
            )
        
    def on_stop(self):
        print("Saindo...")
        self.driver.quit()  
        
class SeleniumUser(User):
    wait_time = constant(1)
    tasks = [tarefas]
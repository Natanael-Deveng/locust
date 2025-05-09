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
        self.driver.get("https://www.americanas.com.br")
        print("Foi pra home")
        
    @task
    def go_to_celulares(self):
        print("Entrou no go_to_celulares")
        href = '/especial/oferta-do-dia?chave=prf_hm_0_tt_7_'
        oferta_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//a[@data-testid="fs-link" and @href="{href}"]')))
        oferta_btn.click()
        print("Chegou na oferta do dia")    
        
    def on_stop(self):
        print("Saindo...")
        self.driver.quit()  
        
class SeleniumUser(User):
    wait_time = constant(5)
    tasks = [tarefas]
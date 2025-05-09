from locust import User, task, events, constant, SequentialTaskSet
import time
from selenium_client import SeleniumClient, By

class tarefas(SequentialTaskSet):
    def on_start(self):
        self.selenium = SeleniumClient(headless=True)

    @task
    def home_page(self):
        start_time = time.time()
        try:
            self.selenium.get("https://www.americanas.com.br")
            print("Foi pra home")
            SeleniumClient.report_locust_event(events, "home_page", start_time)
        except Exception as e:
            SeleniumClient.report_locust_event(events, "home_page", start_time, exception=e)
        
    @task
    def go_to_celulares(self):
        start_time = time.time()
        try:
            print("Entrou no go_to_celulares")
            self.selenium.wait_and_click_xpath(By.XPATH, '//a[@data-testid="fs-link" and @href="/especial/oferta-do-dia?chave=prf_hm_0_tt_7_"]', 10)
            print("Chegou na oferta do dia")
            SeleniumClient.report_locust_event(events, "go_to_celulares", start_time)
        except Exception as e:
            SeleniumClient.report_locust_event(events, "go_to_celulares", start_time, exception=e)

    def on_stop(self):
        print("Saindo...")
        self.selenium.quit()

class SeleniumUser(User):
    wait_time = constant(1)
    tasks = [tarefas]
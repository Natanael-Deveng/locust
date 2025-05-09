from locust import task, constant, HttpUser

headers = {
    "Content-Type": "text/xml; charset=utf-8",
    "SOAPAction": "http://tempuri.org/Add"
}
body = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <Add xmlns="http://tempuri.org/">
      <intA>7</intA>
      <intB>5</intB>
    </Add>
  </soap:Body>
</soap:Envelope>"""

class Teste(HttpUser):
    wait_time = constant(3)
    host = "http://www.dneonline.com"
    
    @task
    def calculator(self):
      # Enviar a requisição SOAP
      self.client.post(
        "/calculator.asmx",
        data=body,
        headers=headers,
      )
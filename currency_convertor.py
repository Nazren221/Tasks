import requests
import json
import time
class WebApi:
   
    def __init__(self,from_,to):
       
        self.url = "https://api.exchangeratesapi.io/latest?base="
        self.from_ = from_
        self.to = to
        self.rates = None
       
    def getJsonformAPI(self):
       
        self.rates=requests.get(self.url+self.from_)
        self.rates=json.loads(self.rates.text)
class Convertor:
    def __init__(self,api):
        self.api = api
       
    def convertor(self,currency):
       
        return api.rates["rates"][api.to.upper()] * currency
       
               
if __name__ == "__main__":
    currency_from = input("Çevirmək istədiyiniz pul vahidini yazın : ").upper()
    currency_to = input("Əvəz ediləcək pul vahidini yazın : ").upper()
    amount = float(input("Miqdar daxil edin : "))
 
    api = WebApi(currency_from,currency_to)
    api.getJsonformAPI()
    convertor = Convertor(api)
    print(f'{amount} {currency_from} = {convertor.convertor(amount)} {currency_to}')
    print(f'{1} {currency_from} = {convertor.convertor(1)} {currency_to}')
   
    print("Təşəkkür edirik.")
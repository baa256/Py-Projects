import alpaca_trade_api as tradeapi
import time

key = ""
sec = ""


url = "https://paper-api.alpaca.markets"

api = tradeapi.REST(key, sec, url, api_version='v2')


account = api.get_account()

print(account.status)

order = api.submit_order(symbol='FB' ,
                         qty = '10' ,
                         side='buy',
                         type='limit',
                         limit_price = '270' ,
                         time_in_force='day')
print(order)

time.sleep(3)3

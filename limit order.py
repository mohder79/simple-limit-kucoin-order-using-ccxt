

import ccxt  
from pprint import pprint

exchange = ccxt.kucoin({
    'apiKey': '**apiKey***',
    'secret': '**secret***',
    'password': '**password***',

})

markets = exchange.load_markets()
print(exchange)


symbol = 'LUNA/USDT'
amount = 3000
price = 0.0001
type = 'limit'
side = 'buy'

params = {
    "reduce_only": True
}

exchange.verbose = True

order = exchange.create_order(symbol, type, side, amount, price, params)

pprint(order)

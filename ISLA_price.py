from pycoingecko import CoinGeckoAPI
import datetime
import pandas as pd

cg = CoinGeckoAPI()

data = cg.get_coin_market_chart_by_id('insula', 'usd', 360)

dates = [datetime.datetime.fromtimestamp(data['prices'][i][0] / 1000).strftime('%Y-%m-%d') for i in range(len(data['prices']))]
price  = [data['prices'][i][1] for i in range(len(data['prices']))]
marketCap  = [data['market_caps'][i][1] for i in range(len(data['prices']))]
volume  = [data['total_volumes'][i][1] for i in range(len(data['prices']))]

print(price)

df_data = {'Date' : dates, 'Price': price, 'Market Cap': marketCap, 'Volume':volume} 
df = pd.DataFrame(df_data)

df.to_csv('ISLA_graph.csv', index=False)
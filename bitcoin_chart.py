from pycoingecko import CoinGeckoAPI
import pandas as pd
import plotly.offline as plotly
import plotly.graph_objs as go

plot = plotly.plot

cg = CoinGeckoAPI()

bitcoin_data = cg.get_coin_market_chart_by_id(id="bitcoin", vs_currency="usd", days=90)
bitcoin_price_data = bitcoin_data["prices"]
data= pd.DataFrame(bitcoin_price_data, columns=["TimeStamp", "Price"])
data["Date"] = pd.to_datetime(data["TimeStamp"], unit="ms")
candlestick_data = data.groupby(data.Date.dt.date).agg({"Price": ["min", "max", "first" , "last"]})

fig = go.Figure(data=[go.Candlestick(x= candlestick_data.index, 
open = candlestick_data["Price"]["first"], 
high = candlestick_data["Price"]["max"], 
low = candlestick_data["Price"]["min"], 
close=candlestick_data["Price"]["last"])])

fig.update_layout(xaxis_rangeslider_visible=False, xaxis_title="Date", yaxis_title="Price (USD $)", title = "Bitcoin Candlestick Chart Over Past 90 Days. <br>It's my first Project on my Data Science's Journey. <br>Powered by Victor Codes. <br><a>victorcodes.tech</a>")

plot(fig, filename ="bitcoin_candlestick_graph.html")

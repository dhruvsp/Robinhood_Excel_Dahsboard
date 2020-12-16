# Install robinhood API Library
pip install robin_stocks

#Required Library
import robin_stocks 
import pandas as pd
import matplotlib.pyplot as plt

#LoggingIn into Robinhood and Enter Authentication number
robin_stocks.login("YourUserID","YourPassword")

#Accessing the Purchased Stock Data
my_stocks = robin_stocks.build_holdings()

#Converting into Dataframe for better Visualization
stock_list = pd.DataFrame(my_stocks)
stock_list = stock_list.T
stock_list['ticker'] = stock_list.index

#Dropping Unnessesary Colmun and Adding new parameter for calculation
stock_list = stock_list.reset_index(drop=True)
stock_list['quantity'] = stock_list['quantity'].astype(float)
stock_list['average_buy_price'] = stock_list['average_buy_price'].astype(float)
stock_list["total_stock_price"] = stock_list["quantity"]*stock_list["average_buy_price"]
stock_list.loc['Total Money Invested'] = pd.Series(stock_list['total_stock_price'].sum(), index = ['total_stock_price'])

#Converting Pandas dataframe into Excel File
data = pd.DataFrame(dct)  
stock_list.drop(['id','type'], axis=1)
stock_list.to_excel("StockList.xlsx")

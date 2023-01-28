import numpy as np
import pandas as pd
import yfinance as yf

import matplotlib.pyplot as plt
import gif

# settings
plt.style.use("seaborn")
gif.options.matplotlib["dpi"] = 300

df = yf.download("TSLA", 
                 start="2019-01-01", 
                 end="2022-12-31")

tsla_df = df[["Adj Close"]].resample("M").last()
@gif.frame
def helper_plot_1(df, i):
    df = df.copy()
    df.iloc[i:] = np.nan
    ax = df.plot(title="Tesla's stock price", legend=False, style="o--")
    ax.set_xlabel("")
    ax.set_ylabel("Price ($)")

frames = []
for i in range(1, len(tsla_df)):
    frames.append(helper_plot_1(tsla_df, i))

gif.save(frames, "tesla_stock_price.gif", 
         duration=15)

df = yf.download(["TSLA", "MSFT", "GOOGL", "AMZN", "AAPL", "NFLX"], 
                 start="2019-01-01", 
                 end="2022-12-31")

df = df[["Adj Close"]].droplevel(0, axis=1).resample("M").last()
df = df.div(df.iloc[0])
df.head()

@gif.frame
def helper_plot_2(df, i):
    
    df = df.copy()
    df.iloc[i:] = np.nan
    
    ax = df.plot(title="Selected stocks' change of value")
    ax.set_xlabel("")
    
    # move the legend below the plot
    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1,
                     box.width, box.height * 0.9])
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.1),
              fancybox=True, shadow=True, ncol=5)
    
    frames = []
for i in range(1, len(df)):
    frames.append(helper_plot_2(df, i))

gif.save(frames, "stock_value.gif", 
         duration=15)
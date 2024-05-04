# filename: stock_price_plot_yfinance.py
import yfinance as yf
import matplotlib.pyplot as plt

# Fetching NVDA and TSLA stock data
nvda = yf.Ticker("NVDA")
tsla = yf.Ticker("TSLA")

nvda_data = nvda.history(period="ytd")["Close"]
tsla_data = tsla.history(period="ytd")["Close"]

# Plotting the data
plt.figure(figsize=(12, 6))
nvda_data.plot(label='NVDA')
tsla_data.plot(label='TSLA')
plt.title('NVDA vs TSLA Stock Price Change YTD')
plt.xlabel('Date')
plt.ylabel('Stock Price (USD)')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Saving the plot to a file
plt.savefig('plot.png')
plt.show()
from flask import Flask, render_template, send_file, request
import yfinance as yf
import pandas as pd
import talib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from io import BytesIO

app = Flask(__name__)

# Function to fetch intraday stock data
def fetch_intraday_data(ticker_symbol, interval="15m"):
    stock_data = yf.download(ticker_symbol, interval=interval, period="1d")
    return stock_data

# Function to detect candlestick patterns
def detect_candlestick_patterns(data):
    data.columns = data.columns.get_level_values(0)
    data = data.rename(columns={'open': 'Open', 'high': 'High', 'low': 'Low', 'close': 'Close'})
    data.dropna(subset=['Open', 'High', 'Low', 'Close'], inplace=True)

    data['Pattern'] = np.nan
    patterns = ['DOJI', 'HAMMER', 'ENGULFING']

    for pattern in patterns:
        pattern_func = getattr(talib, f"CDL{pattern}")
        open_arr, high_arr, low_arr, close_arr = data['Open'].values, data['High'].values, data['Low'].values, data['Close'].values

        if len(open_arr) == len(high_arr) == len(low_arr) == len(close_arr):
            pattern_result = pattern_func(open_arr, high_arr, low_arr, close_arr)
            data['Pattern'] = data['Pattern'].where(pattern_result == 0, pattern.capitalize())

    return data

# Function to plot candlestick chart with patterns
def plot_candlestick_with_patterns(data, ticker_symbol):
    fig, ax = plt.subplots(figsize=(10, 6))

    for i in range(len(data)):
        color = 'green' if data['Close'].iloc[i] > data['Open'].iloc[i] else 'red'
        timestamp = mdates.date2num(data.index[i])

        ax.plot([timestamp, timestamp], [data['Low'].iloc[i], data['High'].iloc[i]], color=color, lw=0.8)
        ax.add_patch(plt.Rectangle((timestamp - 0.005, min(data['Open'].iloc[i], data['Close'].iloc[i])),
                                   width=0.01, height=abs(data['Close'].iloc[i] - data['Open'].iloc[i]), color=color))

    pattern_colors = {'Doji': 'blue', 'Hammer': 'green', 'Engulfing': 'red'}
    for pattern_name, pattern_data in data[data['Pattern'].notna()].groupby('Pattern'):
        pattern_timestamps = [mdates.date2num(ts) for ts in pattern_data.index]
        ax.scatter(pattern_timestamps, pattern_data['Close'],
                   color=pattern_colors.get(pattern_name, 'orange'), label=pattern_name, s=50, zorder=5)

    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
    ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))
    plt.xticks(rotation=45)

    ax.set_xlabel('Time')
    ax.set_ylabel('Price')
    ax.set_title(f"{ticker_symbol} Intraday Candlestick Chart with Patterns")
    ax.grid(True)
    ax.legend()

    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close(fig)
    return img

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plot', methods=['POST'])
def plot():
    ticker = request.form.get('ticker', 'WIPRO.NS')  # Default ticker
    data = fetch_intraday_data(ticker)
    data = detect_candlestick_patterns(data)

    img = plot_candlestick_with_patterns(data, ticker)
    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

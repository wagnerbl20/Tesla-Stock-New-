import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

# Function to plot candlestick chart with moving averages and crossover points
def plot_stock_data(symbol):
    # Download stock data
    stock_data = yf.download(symbol, start="2014-02-25", end="2024-02-25")

    # Calculate moving averages
    stock_data['50MA'] = stock_data['Close'].rolling(window=50).mean()
    stock_data['200MA'] = stock_data['Close'].rolling(window=200).mean()

    # Plot candlestick chart
    mpf.plot(stock_data, type='candle', style='charles',
             title='Tesla Stock Price',
             ylabel='Price ($)',
             mav=(50, 200),
             volume=True,
             show_nontrading=True)

    # Plot 50-day and 200-day moving averages
    plt.plot(stock_data['50MA'], color='blue', label='50 Day MA')
    plt.plot(stock_data['200MA'], color='red', label='200 Day MA')

    # Mark crossover points
    crossover_points = []
    for i in range(1, len(stock_data)):
        if (stock_data['50MA'][i] > stock_data['200MA'][i]) != (stock_data['50MA'][i - 1] > stock_data['200MA'][i - 1]):
            crossover_points.append(stock_data.index[i])
    for crossover_point in crossover_points:
        plt.axvline(x=crossover_point, color='black', linestyle='--', alpha=0.5)

    # Show plot
    plt.legend()
    plt.show()

# Main function
if __name__ == "__main__":
    plot_stock_data('TSLA')

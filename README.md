# 📈 Simple Moving Average (SMA) Trading Strategy  

This project implements a basic trading strategy using Moving Averages (MA) to analyze stock price trends.  
It serves as a learning tool for financial data manipulation in Python, focusing on pandas, data visualization, and basic algorithmic trading concepts.  

## ✨ Features  
- Stock Data Processing: Loads stock price data and calculates 10-day (MA10) and 50-day (MA50) moving averages.  
- Trading Logic:  
  - If MA10 > MA50, a long position (buy signal) is taken.  
  - Otherwise, no position is taken.  
- Profit Calculation: Computes daily profit/loss based on the strategy's signals.  
- Data Visualization: Uses Matplotlib to plot profit trends over time.  

## 🛠️ Technologies Used  
- Python: `pandas`, `matplotlib`  
- Data Manipulation: Rolling window functions for calculating moving averages  
- Algorithmic Trading Basics: Simple buy/sell conditions based on moving average crossovers  

## 🚀 How It Works  
1. Import stock price data (Microsoft in this case).  
2. Compute moving averages (MA10 & MA50) using rolling mean.  
3. Define buy conditions: If MA10 crosses above MA50, enter a position.  
4. Calculate daily profit/loss by checking the next day's closing price.  
5. Visualize the profit trend using Matplotlib.  

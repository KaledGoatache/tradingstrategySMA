import pandas as pd
import matplotlib.pyplot as plt

#Load Microsoft's stock data using the correct method
try:
    ms = pd.read_csv('/Users/kaledgoatache/Desktop/a programming/python/microsoft.csv')  #Update the file path if necessary
except FileNotFoundError:
    print("CSV file not found. Please check the file path.")
    exit()

#Add moving averages: MA10 and MA50
ms['MA10'] = ms['Close'].rolling(window=10).mean()
ms['MA50'] = ms['Close'].rolling(window=50).mean()

#Drop rows with NaN values after moving average calculations
ms.dropna(inplace=True)

#Display the first few rows to confirm the data is loaded correctly
print(ms.head())

#Add a new column "Shares": 1 if MA10 > MA50, else 0
ms['Shares'] = ms.apply(lambda row: 1 if row['MA10'] > row['MA50'] else 0, axis=1)

#Add a new column "Close1" for tomorrow's close price
ms['Close1'] = ms['Close'].shift(-1)

#Calculate "Profit" based on trading strategy
ms['Profit'] = ms.apply(lambda row: row['Close1'] - row['Close'] if row['Shares'] == 1 else 0, axis=1)

#Plot Profit/Loss
plt.figure(figsize=(12, 6))
ms['Profit'].plot(title='Profit/Loss from Trading Strategy')
plt.axhline(y=0, color='red', linestyle='--', label='Break-even')
plt.legend()
plt.show()

#Calculate accumulated wealth using cumsum()
ms['wealth'] = ms['Profit'].cumsum()

#Display the last few rows to check final wealth
print(ms.tail())

#Plot the accumulated wealth over time
plt.figure(figsize=(12, 6))
ms['wealth'].plot(title='Accumulated Wealth Over Time', color='green')
plt.title(f"Total profit: ${ms['wealth'].iloc[-2]:.2f}")
plt.xlabel('Date')
plt.ylabel('Wealth')
plt.show()
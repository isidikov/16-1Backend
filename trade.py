import pandas_datareader as pdr
import pandas as pd

# Загрузка данных о ценах на золото с помощью Yahoo Finance
data = pdr.get_data_yahoo('XAUUSD=X', start='2022-01-01', end='2022-12-31')

# Рассчитываем скользящие средние
data['SMA_50'] = data['Close'].rolling(window=50).mean()
data['SMA_200'] = data['Close'].rolling(window=200).mean()

# Генерация сигналов
data['Signal'] = 0
data.loc[data['SMA_50'] > data['SMA_200'], 'Signal'] = 1  # Сигнал на покупку
data.loc[data['SMA_50'] < data['SMA_200'], 'Signal'] = -1  # Сигнал на продажу

# Вывод сигналов
print(data[['Close', 'SMA_50', 'SMA_200', 'Signal']])

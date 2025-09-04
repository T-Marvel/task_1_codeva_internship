#import libraries
import pandas as pd

#increase number of viewable rows
pd.options.display.max_rows = 1000

#Read iris.csv
df = pd.read_csv('2) Stock Prices Data Set.csv')

#Clean Data: null values, duplicates and inconsistencies
cleaned_df = df.drop_duplicates(keep="last")
open_mean = round(df['open'].mean(), 4)
high_mean = round(df['high'].mean(), 4)
low_mean = round(df['low'].mean(), 4)
cleaned_df = df.fillna({'open': open_mean,'high': high_mean,'low': low_mean})
cleaned_df['symbol'] = cleaned_df['symbol'].str.replace('[^a-zA-Z0-9 ]','', regex=True)
cleaned_df.to_csv('cleaned_Stock_Prices_Set.csv', index=False)
print(cleaned_df)

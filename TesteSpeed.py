from datetime import datetime
from threading import Timer

import pandas as pd
import speedtest


# Function to collect data regarding internet speed and save in csv format
def internet():
    df = pd.read_excel('data_collected.xlsx', sheet_name='base')
    s = speedtest.Speedtest()
    curr_date = datetime.now().strftime('%d/%m/%Y')
    curr_time = datetime.now().strftime('%H:%M')
    internet_speed = s.download(threads=None)*(10**-6)
    df.loc[len(df)] = [curr_date, curr_time, internet_speed]
    df.to_excel('data_collected.xlsx', sheet_name='base', index=False)
    print(df)
    Timer(50, internet).start()

internet()

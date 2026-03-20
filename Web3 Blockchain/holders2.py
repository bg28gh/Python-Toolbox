import os
import pandas as pd
dir_route = 'C:\\Users\\bauti\\Desktop\\Codigos\\Crypto\\coins'
initial = None
for csv_route in os.listdir(dir_route):

    if initial == None:
        initial = set(pd.read_csv(os.path.join(dir_route, csv_route))['From'])
    else:
        initial &= set(pd.read_csv(os.path.join(dir_route, csv_route))['From'])

print(initial)
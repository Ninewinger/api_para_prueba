from operator import index
import pandas as pd
import json

df = pd.read_excel("C:/Users/x_zer/Documents/intento 2/prueba entrevista/202112_PUB_TRINT.xlsb", engine='pyxlsb', index=False)

#remove nan and unnamed columns
df = df.dropna(axis=1, how='all')
df = df.dropna(axis=0, how='all')

df.to_csv("C:/Users/x_zer/Documents/intento 2/prueba entrevista/202112_PUB_TRINT.csv", index=False, encoding='utf-8-sig')

on_csv = pd.read_csv("C:/Users/x_zer/Documents/intento 2/prueba entrevista/202112_PUB_TRINT.csv", encoding='utf-8-sig', index=False)





print(on_csv)
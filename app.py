from operator import index
import pandas as pd
import json

""" df = pd.read_excel("C:/Users/x_zer/Documents/intento 2/prueba entrevista/202112_PUB_TRINT.xlsb", engine='pyxlsb')

#remove nan
df = df.dropna(axis=0, how='any')

df.to_csv("C:/Users/x_zer/Documents/intento 2/prueba entrevista/202112_PUB_TRINT.csv", index=False, encoding='utf-8-sig', header=False, index_label=False) """

on_csv = pd.read_csv("C:/Users/x_zer/Documents/intento 2/prueba entrevista/202112_PUB_TRINT.csv", encoding='utf-8-sig')

on_csv.to_json("C:/Users/x_zer/Documents/intento 2/prueba entrevista/202112_PUB_TRINT.json", orient='records', force_ascii=False)

on_json = pd.read_json("C:/Users/x_zer/Documents/intento 2/prueba entrevista/202112_PUB_TRINT.json", orient='records', encoding='utf-8-sig')

print(on_json)
import os
import pandas as pd


data = []
for root, dirs, files in os.walk("evidencias"):
    for filename in files:
        data.append((filename, root))

df1 = pd.DataFrame(data, columns=['nome', 'pasta'])

df1.to_excel('arquivos-ev.xls')


data = []
for root, dirs, files in os.walk("evidencias-safe"):
    for filename in files:
        data.append((filename, root))

df2 = pd.DataFrame(data, columns=['nome', 'pasta'])

df2.to_excel('arquivos-safe.xls')

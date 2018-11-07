import pandas as pd
import numpy as np


def normaliza_nomes(pandas_series):

    original_names = pandas_series
    df['nome_fantasia'] = df.name.str.upper()
    for i in range(4):
        df['nome_fantasia'] = df.nome_fantasia.str.replace('( ME(.)?| LTDA(.)?| S(.)?A(.)?)$', '', regex=True)


    df['nome_fantasia'] = df.nome_fantasia.str.replace(' DE | DAS | DOS | E ', ' ', regex=True)
    df['nome_fantasia'] = df.nome_fantasia.str.replace('( DE)$|( DAS)$|( DOS)$|( E)$', ' ', regex=True)
    df['nome_fantasia'] = df.nome_fantasia.str.replace(' DA | DO ', ' ', regex=True)
    df['nome_fantasia'] = df.nome_fantasia.str.replace('( DA)$ |( DO)$ ', ' ', regex=True)
    df['nome_fantasia'] = df.nome_fantasia.str.strip()
    df['nome_fantasia'] = df.nome_fantasia.str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')

return nome_fantasia

# df[['name', 'nome_fantasia']]

nomes = [
        'maria machado do socorro ltda',
        'ME ltda.',
        'ME ltda',
        'SA Ltda',
        'SA ltda.',
        'SA S/A',
        'SA S/A.',
        'SA S.A.',
        'josiade de desgraça',
        'josiada da dada',
        'josiado do dodo',
        'roselinildo do dolar ltda',
        'escadas das datas ME',
        'escadas das datas ME.',
        'landos dos doses Ltda me S.A.',
        'landos dos doses Ltda me S.A',
        'landos dos doses Ltda me S/A',
        'josé de descartes ME',
        'jose de descartes ltda',
        'aviação paulista SA',
        'aviacao paulista de SA'
    ]

series = pd.Series({'name': nomes})

nome_fantasia = normaliza_nomes(series)

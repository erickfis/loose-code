import pandas as pd
import numpy as np


def normaliza_nomes(original_names):
    """
    Normalize names.

    Normalize names in a pd.Series by:
        - upper casing
        - removing LTDA / SA / ME designators
        - removing prepositions
        - striping spaces
        - removing accents
    """

    nome_fantasia = original_names.str.upper()

    for i in range(4):
        nome_fantasia = nome_fantasia.str.replace('( ME(.)?| LTDA(.)?| S(.)?A(.)?)$', '', regex=True)

    nome_fantasia = nome_fantasia.str.replace(' DE | DAS | DOS | E ', ' ', regex=True)
    nome_fantasia = nome_fantasia.str.replace('( DE)$|( DAS)$|( DOS)$|( E)$', ' ', regex=True)
    nome_fantasia = nome_fantasia.str.replace(' DA | DO ', ' ', regex=True)
    nome_fantasia = nome_fantasia.str.replace('( DA)$ |( DO)$ ', ' ', regex=True)
    nome_fantasia = nome_fantasia.str.strip()

    nome_fantasia = nome_fantasia.str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')

    return nome_fantasia

def testing():
    """Produces an example of this function"""
    
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

    df = pd.DataFrame({'name': nomes})
    df['nome_fantasia'] = normaliza_nomes(df.name)

    print(df)
    return


if __name__ == '__main__':
    testing()

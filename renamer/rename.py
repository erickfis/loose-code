import os
from distutils.dir_util import copy_tree
import pandas as pd


def cria_lista():
    """Cria lista de arquivos."""
    data = []

    for root, dirs, files in os.walk("."):
        for filename in files:
            data.append((filename, root))

    df = pd.DataFrame(data, columns=['nome', 'pasta'])
    df.to_excel('arquivos.xls')


def renamer():
    """Rename - mantem nome do arquivo após o primeiro espaço."""
    safe = 'C:/Users/erick.gomes/Desktop/erickfis/projetos/temp/renamer/renomeados'
    original = 'C:/Users/erick.gomes/Desktop/erickfis/projetos/temp/renamer/src'
    # safe = os.path.join(caminho, 'renomeados')
    os.mkdir(safe)
    copy_tree(original, safe)

    for subdir, dirs, files in os.walk(safe):
        for filename in files:
            newFilename = filename.split(' ')[1:]
            newFilename = ' '.join(newFilename)

            filePath = os.path.join(subdir, filename)
            new_filePath = os.path.join(subdir, newFilename)

            # print(f'novo: {new_filePath}')
            # print(f'velho: {filePath}')
            os.rename(filePath, new_filePath)  # rename your file

    return print('done')


renamer()

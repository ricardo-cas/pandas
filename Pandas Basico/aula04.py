import pandas as pd

# importando dados 
dados = pd.read_csv('db.csv', sep = ';', index_col=0)

# Iterando DataFrames
def carrega_dados():
    dados = pd.read_csv('db.csv', sep = ';', index_col=0)
    print(dados.head())

def iterando_dataset():
    # dados = pd.read_csv('db.csv', sep = ';', index_col=0)
    for index, linha in dados.iterrows():
        if (2020 - linha['Ano'] != 0):
            dados.loc[index, 'Km_media'] = linha['Quilometragem'] / 2020 - linha['Ano']
        else:
            dados.loc[index, 'Km_media'] = 0
print(dados.describe())

def __main():
    carrega_dados()
    iterando_dataset()


if __name__ == "__main__":
    __main()

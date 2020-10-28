import pandas as pd

# Tratamento de dados

dados = pd.read_csv('db.csv', sep = ';', index_col=0)

def __main():
    print('Pandas Starting....')
    print(dados.head())
    print('\n')
    # Mostra algumas informações do Dataset de forma rápida
    print(dados.info())

if __name__ == "__main__":
    __main()
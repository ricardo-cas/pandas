import pandas as pd

def inicializa_base():
    base = pd.read_csv('./aluguel.csv',sep=';')
    print(f'10 primeiras informações da Base:\n{base.head(10)}\n')
    print(f'\n Estatisticas de todos as colunas que possuem número:')
    print(base.value_counts())
    print(f'\n')
    print(f'\nTamanho da base: {base.shape[0]} Observações e colunas {base.shape[1]}')
    print(f'\nValores estatísticos da base:\n{base.describe()}')
    print(f'\nÚltimos valores da base:\n{base.tail()}')
    print(base.groupby)

if __name__ == "__main__":
    inicializa_base()

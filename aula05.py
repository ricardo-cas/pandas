import pandas as pd

# Tratamento de dados

dados = pd.read_csv('db.csv', sep = ';', index_col=0)

def carrega():
    print('Pandas Starting....')
    print(dados.head())
    print('\n')
    # Mostra algumas informações do Dataset de forma rápida
    print(dados.info())


def __main():
    carrega()
    selecionando_informacoes_nulas()
    substituindo_informacoes_nulas


def selecionando_informacoes_nulas():
    print('selecionando os valores nulos da coluna "Quilometragem" \n')
    dados.Quilometragem.isna()
    print('\n')
    print('Retorno dos valores nulos da coluna "Quilometragem" em forma de Series \n')
    print(dados.Quilometragem.isna())
    print('\n')
    print('Com essas Series podemos passar ela para o DataFrame em forma de Paramêtro, para que ele faça um Select \n')
    print(dados[dados.Quilometragem.isna()])
    print('\n')

def substituindo_informacoes_nulas():
    print('Hello')

if __name__ == "__main__":
    __main()
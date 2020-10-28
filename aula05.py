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
    substituindo_informacoes_nulas()
    eliminando_valores_nulos_no_dataframe()


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
    print('Aqui estou modificando somente visualmente os dados nulos por 0, não está gravando efetivamente no DataFrame')
    dados.fillna(0)
    print(dados.fillna(0))
    print('\n')
    print('Aqui estou modificando os dados nulos por 0, e gravando efetivamente no DataFrame')
    dados.fillna(0, inplace = True)
    print('\n')
    print(dados)


def eliminando_valores_nulos_no_dataframe():
    import pandas as pd
    carros = pd.read_csv('db.csv', sep= ';')
    print('### Novo Data Frame ### \n')
    print(carros.head())
    print('Eliminando os dados nulos do DataFrame utiliando o metodo Dropna: \n')
    # utilizando o dropna você precisa falar qual coluna que você quer que ele procure os dados à serem deletados do DataFrame
    # E para que essa remoção seja efetiva, é necessário passar o paramento inplace = True
    carros.dropna(subset = ['Quilometragem'], inplace = True)
    print('Resultado da eliminação: \n')
    print(carros)

if __name__ == "__main__":
    __main()
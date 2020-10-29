import pandas as pd

def carrega():
    dados = pd.read_csv('aluguel.csv', sep= ';')
    print(dados.head(10))

def tipo_de_dados_do_dataframe():
    dados = pd.read_csv('aluguel.csv', sep= ';')
    print('\n')
    print('Exibindo os tipos de dados do arquivo importado')
    print(pd.DataFrame(dados.dtypes))
    print('\n')
    print('ajustando o nome da coluna que o metodo dtypes retorna na visualização')
    print(pd.DataFrame(dados.dtypes, columns = ['Tipo de Dados']))

def main():
    carrega()
    tipo_de_dados_do_dataframe()


if __name__ == "__main__":
    main()
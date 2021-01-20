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
    print('Ajustando o nome da coluna que o metodo dtypes retorna na visualização')
    print(pd.DataFrame(dados.dtypes, columns = ['Tipo de Dados']))
    print('\n')
    print('Atribuindo um título para a coluna de index \n')
    tipo_de_dados = pd.DataFrame(dados.dtypes, columns = ['Tipo de Dados'])
    tipo_de_dados.columns.name = 'Variaveis'
    print(tipo_de_dados)

def quantidade_de_observacoes():
    print('\n')
    print('Mostra a quantidade de observações e variaveis da base')
    dados = pd.read_csv('aluguel.csv', sep= ';')
    dados.shape
    print(dados.shape)
    print('\n')
    print('Exibindo somente a quantidade de observações da base de dados')
    print(dados.shape[0])
    print('\n')
    print('Exibindo somente a quantidade de variaveis que existem na base de dados')
    print(dados.shape[1])
    print('\n')
    print('Exibindo as duas informações de uma maneira unica:')
    print('A base possuíu {} registros e {} variáveis'.format(dados.shape[0], dados.shape[1]))

def main():
    carrega()
    tipo_de_dados_do_dataframe()
    quantidade_de_observacoes()

if __name__ == "__main__":
    main()
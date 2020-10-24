import pandas as pd

# Lendo o arquivo CSV
dados = pd.read_csv('db.csv', sep = ';')

# Classe para ler arquivo CSV
def ler_arquivo_csv():
    # _Para fazer a leitura de um CSV, utilizamos o comendo 'read_csv'
    # Aqui estou definndo que os meus dados devem ser do arquivo 'db.csv' e que ele utiliza o separado ';' para identificar as colunas
    dados = pd.read_csv('db.csv', sep = ';')
    print(dados.head()) # função 'Head' mostra os 5 primeiros registros do dataframe "dados"

# Métodos dessa seção são relacionados a seleção de dados do DataFrame 'dados'
def seleciona_coluna():
    print('#########'*16)
    print('Selecionando colunas:')
    print(dados['Ano'])
    print(dados[['Nome','Ano']])

def seleciona_linhas():
    # Selecionando linhas - [ i : j ] 
    # Observação: A indexação tem origem no zero e nos fatiamentos (*slices*) a linha com índice i é incluída e a linha com índice j não é incluída no resultado.
    print('Selecionando linhas')
    print('#########'*16)
    print(dados[:27])

if __name__ == "__main__":
    ler_arquivo_csv()
    print('#########'*16)
    seleciona_coluna()
    print('#########'*16)
    seleciona_linhas()
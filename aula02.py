import pandas as pd

# Lendo o arquivo CSV
dados = pd.read_csv('db.csv', sep = ';')

# Classe para ler arquivo CSV
def ler_arquivo_csv():
    # _Para fazer a leitura de um CSV, utilizamos o comendo 'read_csv'
    # Aqui estou definindo que os meus dados devem ser do arquivo 'db.csv' e que ele utiliza o separado ';' para identificar as colunas
    # Indicando o índice que deve ser utilizado, baseado no arquivo importado.
    dados = pd.read_csv('db.csv', sep = ';', index_col = 0)
    # função 'Head' mostra os 5 primeiros registros do dataframe "dados"
    print(dados.head()) 

# Métodos dessa seção são relacionados a seleção de dados do DataFrame 'dados'

def selecionando_uma_coluna():
    print('Selecionando uma Coluna \n')
    print(dados['Valor'])
    print(f'O Tipo dessa estrutura é:')
    print(type(dados['Valor']))
    print('\n')

def seleciona_linhas():
    # Selecionando linhas - [ i : j ] 
    # Observação: A indexação tem origem no zero e nos fatiamentos (*slices*) a linha com índice i é incluída e a linha com índice j 
    # não é incluída no resultado.
    print('Selecionando linhas de 0 à 27:\n')
    print(dados[:27])
    print('#########'*16)
    print('\n')

def transformando_series_em_dataframe():
    print('Transformando as informações da coluna "[Valor]" em um Data Frame \n')
    # Adicionando um [] dentro da estrutura da série, é possível transformar o resultado para um Data Frame
    print(dados[['Valor']])    
    print('\n')
    print(f'O Tipo dessa estrutura é:')
    print(type(dados[['Valor']]))
    print('\n')

def utilizando_iloc_para_seleções():
    dados['Valor']
    print('*-#*-#*-#'*16)
    print('Outra forma de seleções é o ".iloc", que faz: \n')
    print('Seleciona com base nos índices, ou seja, se baseia na posição das informações.')
    print('\n')
    print(dados.iloc[0])
    print('*-#*-#*-#'*16)

def usando_iloc_para_selecionar_linhas_e_colunas():
    # O iLoc seleciona com base nos indíces da Series ou DataFrame
    # Com isso, é possível definir não só a quantidade de registros que você receberá o retorno, como também quais colunas você quer visualizar
    dados.iloc[0:28, [0,5,2]]
    # Na linha abaixo estou definindo que só quero que seja exibido os dados do índice 0 até o 27
    # e logo após essa definição, estou  definindo quais colunas que eu quero que o método 'iloc' retorne para visualização.
    print('\n')
    print(dados.iloc[0:28, [0,5,2]])
    print('*-#*-#*-#'*16)
    print('\n')

def __main():
    ler_arquivo_csv()
    print('#########'*16)
    print('\n')
    selecionando_uma_coluna()
    seleciona_linhas()
    transformando_series_em_dataframe()
    utilizando_iloc_para_seleções()
    usando_iloc_para_selecionar_linhas_e_colunas()


if __name__ == "__main__":
    __main()


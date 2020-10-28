import pandas as pd

dados = pd.read_csv('db.csv', sep = ';', index_col=0)

def carrega_base_de_dado():
    dados = pd.read_csv('db.csv', sep = ';', index_col=0)
    print(dados.head())
    print(dados.describe())

def __main():
    carrega_base_de_dado()
    seleciona_toda_coluna_motor()
    selecionar_todos_os_carros_com_motor_a_diesel()
    selecionando_duas_opcoes_na_consulta()
    utilizando_metodo_query()

def seleciona_toda_coluna_motor():
    carrega_base_de_dado()
    print('Seleciona toda a coluna [Motor] e retorna uma Series\n')
    print(dados.Motor)
    print('°(^-^)°'*10)
    print(type(dados.Motor))
    print('\n')
    print('°(^-^)°'*10)
    
def selecionar_todos_os_carros_com_motor_a_diesel():
    print('<°(^-^)°>'*10)
    print('\n')
    
    print('Seleciona toda a coluna [Motor] a diesel \n Retorna uma Series Boleana')
    print(dados.Motor == 'Motor Diesel')
    
    print('Selecionando todos os carros com motor a Diesel \n')
    # Fazendo uma consulta, utilizando a querie a seguir:
    carros_a_diesel = dados.Motor == 'Motor Diesel'
    print(f'Tipo dos dados é: {type(carros_a_diesel)}')
    # É possível passar o resultado da querie como parâmentro pro DataFrame e assim ele retornará aquele resultado
    print(dados[carros_a_diesel])
    # realizando os Describe para obter informações resumidas sobre o DataFrame
    print(dados[carros_a_diesel].describe())
    # Verificando somente as informações do topo do DataFrame
    print(dados[carros_a_diesel].head())
    
def selecionando_duas_opcoes_na_consulta():
    print('<°(^-^)°>'*10)
    print('\n')
    # Para fazer uma consulta com duas condições é importante sempre colocar o () para separar as condições e também utilizar os simbolos de operações condicionais
    dados[(dados.Motor == 'Motor Diesel') & (dados.Zero_km == True)]
    print(dados[(dados.Motor == 'Motor Diesel') & (dados.Zero_km == True)])

def utilizando_metodo_query():
    print('<°(^-^)°>'*10)
    print('\n')
    # Outra maneira de fazer a consulta é utilizando o método query do Python
    # A Diferença entre esse método é que nele você passa direto as colunas e utiliza notação SQL para as condições (and, or)
    dados.query('Motor == "Motor Diesel" and Zero_km == True')
    print(dados.query('Motor == "Motor Diesel" and Zero_km == True'))

if __name__ == "__main__":
    __main()
import pandas as pd

# Lendo o arquivo CSV
dados = pd.read_csv('db.csv', sep = ';')

# Classe para ler arquivo CSV
def ler_arquivo_csv():
    # _Para fazer a leitura de um CSV, utilizamos o comendo 'read_csv'
    # Aqui estou definindo que os meus dados devem ser do arquivo 'db.csv' e que ele utiliza o separado ';' para identificar as colunas
    # Indicando o índice que deve ser utilizado, baseado no arquivo importado.
    dados = pd.read_csv('db.csv', sep = ';', index_col = 0)
    print(dados.head()) # função 'Head' mostra os 5 primeiros registros do dataframe "dados"

def __main():
    ler_arquivo_csv()
    print('#########'*16)

if __name__ == "__main__":
    __main()
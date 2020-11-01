import pandas as pd

def carrega_arquivo_json():
    json = open('extras/dados/aluguel.json')
    # mostrando as informações sobre a variavel
    print('Visualizando o tipo do arquivo que foi lido pelo pandas, utilizando o método OPEN \n')
    print(json) 
    print('Lendo o arquivo no formato JSON \n')
    # para realizar a leitura do arquivo JSON, é necessário utilizar o método .read()
    # por default, ele irá mostrar as informações dos 10 primeiros registros do arquivo
    print(json.read())
    

def importando_json_em_um_data_frame():
    # df é Data Frame
    df_json = pd.read_json('extras/dados/aluguel.json')
    # obtendo o tipo de dados do df_json
    print(type(df_json))
    print('\n')
    print('Visualizando os dados em formato de um DataFrame')
    print('\n')
    print(df_json)


def carrega_arquivo_txt():
    print('Hello arquivo txt')
    # importando arquivo para o pandas
    arquivo_txt = open('extras/dados/aluguel.txt')
    print(arquivo_txt.read())

def importando_txt_em_um_data_frame():
    # Para o pandas ler um arquivo txt utilize o método read_tables()
    # O separador default do metodo é tabulação "\t", estou definindo somente para saber depois
    df_txt = pd.read_table('extras/dados/aluguel.txt', sep="\t")
    print(df_txt.head())

def importando_arquivo_excel():
    # Para ler arquivo excel utilize o método read_excel()
    print('Para conseguir realizar a leitura do arquivo Excel, é necessário instalar "pip install xlrd"')
    arquivo_excel = pd.read_excel('extras/dados/aluguel.xlsx')
    print(arquivo_excel.head())


def main():
    # carrega_arquivo_json()
    # importando_json_em_um_data_frame()
    # carrega_arquivo_txt()
    # importando_txt_em_um_data_frame()
    importando_arquivo_excel()





if __name__ == "__main__":
    main()
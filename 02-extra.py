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

def importando_arquivo_html():
    print('Hello Web')
    # Para ler arquivo html, utilize o método read_html()
    df_html = pd.read_html('extras/dados/dados_html_1.html')
    print(df_html[0])

def lendo_pagina_da_web():
    df_web = pd.read_html('https://www.federalreserve.gov/releases/h3/current/')
    # lendo a quantidade de listas que está dentro do dataframe
    print(len(df_web))
    # Visualizando o conteúdo de cada lista do DF
    print('Visualizando o conteúdo da tabela 1')
    print(df_web[0])
    print('Visualizando o conteúdo da tabela 2')
    print(df_web[1])
    print('Visualizando o conteúdo da tabela 3')
    print(df_web[2])

def finaliza():
    print('\n')
    print('### Consolidando os conhecimentos:')
    print('\n')
    print('- Nesta aula, sobre pandas, aprendemos:')
    print('- Como importar a biblioteca (import pandas as pd)')
    print('- Como ler fontes de dados diferentes:')
    print('- Uma base CSV (pd.read_csv(...))')  
    print('- Uma base JSON (pd.read_json(...))')
    print('- Uma base TXT (pd.read_table(...))')
    print('- Um arquivo EXCEL (pd.read_excel(...)')
    print('- Uma página HTML (pd.read_html(...)')
    print('- Vários métodos e atributos úteis de dataframes, como:')
    print('- info()')
    print('- head()')
    print('- dtypes')
    print('- columns')
    print('- shape')
    print('- E sobre Jupyter, vimos como:')
    print('- Criar diferentes tipos de células dentro do Jupyter')
    print('- Acessar a documentação')
    print('- Como reexecutar todas as células')

def main():
    carrega_arquivo_json()
    importando_json_em_um_data_frame()
    carrega_arquivo_txt()
    importando_txt_em_um_data_frame()
    importando_arquivo_excel()
    importando_arquivo_html()
    lendo_pagina_da_web()
    finaliza()


if __name__ == "__main__":
    main()
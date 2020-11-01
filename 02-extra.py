import pandas as pd

def carrega():
    json = open('extras/dados/aluguel.json')
    # mostrando as informações sobre a variavel
    print(json) 
    print('\n')
    # para realizar a leitura do arquivo JSON, é necessário utilizar o método .read()
    # por default, ele irá mostrar as informações dos 10 primeiros registros do arquivo
    print(json.read())
    



def main():
    carrega()


if __name__ == "__main__":
    main()
import pandas as pd

def carrega():
    dados = pd.read_csv('aluguel.csv', sep= ';')
    print(dados.head(10))



def main():
    carrega()


if __name__ == "__main__":
    main()
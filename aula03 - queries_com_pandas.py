import pandas as pd


def carrega_base_de_dado():
    dados = pd.read_csv('db.csv', sep = ';', index_col=0)
    print(dados.head())
    # print(dados.describe())



def __main():
    carrega_base_de_dado()


if __name__ == "__main__":
    __main()
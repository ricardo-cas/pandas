import pandas as pd

dados = pd.read_csv('db.csv', sep = ';', index_col=0)

def __main():
    print('Pandas Starting....')

if __name__ == "__main__":
    __main()

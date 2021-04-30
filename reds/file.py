import csv
import win32com.client

class File():

    def __init__(self):
        print("teste")


    # @staticmethod
    def retornarLista(self, fileName):
        try:
            arquivo = open(fileName, encoding="utf8")
            leitor = csv.reader(arquivo)
            dados = list(leitor)
            arquivo.close()
            return dados
        except FileNotFoundError:
            print("Não consigo editar o arquivo")
        else:
            print("Não consigo editar o arquivo")
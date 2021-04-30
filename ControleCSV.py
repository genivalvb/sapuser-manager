import csv
from time import time

import win32com.client
from db_dao_smartprocess import *


class LerCSV:
    nlinhas = 0
    dados = []
    num_users = 0


    def __init__(self):
        print("teste")

    def carregarUsers(self):
        try:
            self.replaceAspas('smartprocess.csv') #SUBSTITUI AS ASPAS NO ARQUIVO POR VAZIO
            self.replacePontoVirgula('smartprocess.csv')
            self.tratarQueriesLista('smartprocess.csv')

            nlinhas =0
            arquivo = open('new_smartprocess.csv',encoding="utf8")  #ABRE O ARQUIVO
            leitor = csv.reader(arquivo)
            dados = list(leitor)

            nlinhas = len(dados) #NUMERO DE LINHAS NO ARQUIVO
            global num_users
            num_users = len(dados)

            nlinhas = nlinhas

            #arquivo.close()
            return dados
        except FileNotFoundError:
            #alert(text="You can't file found.", title="AutoSAP Error", button='OK')
            print("You can't file found.")

        except IOError:
            #alert(text="Could not read file:", title="AutoSAP Error", button='OK')
            print("You can't file found.")
        except BaseException as ex:
            print("Carregar dados error: {}".format(ex))
        finally:
            #arquivo.close()
            pass


    @staticmethod
    def replaceAspas(file):
        try:
            with open(file,'U') as f:
                newText = f.read()

                while '"' in newText:
                    newText = newText.replace('"', '')

            with open(file,'w') as f:
                f.write(newText)
        except PermissionError:
            #alert(text="O arquivo " + file + " deve estar aberto, não posso editar.", title="AutoSAP Error", button='OK')
            print("Não consigo editar o arquivo")
        else:
            #alert(text="Problemas em tentativa de editar arquivo: " + file, title="AutoSAP Error", button='OK')
            print("Não consigo editar o arquivo")

    @staticmethod
    def replacePontoVirgula(file):
        with open(file,'U') as f:
            newText = f.read()

            while ';' in newText:
                newText = newText.replace(';', ',')

        with open(file,'w') as f:
            f.write(newText)

    @staticmethod
    def tratarQueriesLista(file):
        try:
            ativar = 0
            fonte = open(file,'r')
            target = 'new_smartprocess.csv'
            nova_linha = ''

            with open(file, 'r') as f:
                for i in f:
                    for a in i:
                        if a == '[': ativar = 1
                        if a == ']': ativar = 10
                        if ativar == 1:
                            if a == ',':
                                nova_linha += '.'
                            else:
                                nova_linha += a
                        else:
                            nova_linha += a


            with open(target, 'w') as arq:
                arq.write(nova_linha)

            print("Acabo de escrever o arquivo")

        except BaseException as ex:
            print("ERRO em corrigir querie: {}:".format(ex))
        finally:

            pass


### CARREGAR A LISTA DE USUÁRIOS DO SAP ###
###
    #@staticmethod
    def carregarListaSAPUsers(self):
        try:
            self.replaceAspas('listasapusers.csv')
            self.replacePontoVirgula('listasapusers.csv')


            nlinhas2 = 0
            arquivo = open('listasapusers.csv',encoding="utf8")
            leitor = csv.reader(arquivo)
            dados = list(leitor)

            return dados
        except FileNotFoundError:
            print("Não consigo editar o arquivo")
        finally:
            arquivo.close()

    def fazer_teste(self):
        lista_users_to_create = self.carregar_ListaSmartProcess()
        #print(lista_users_to_create[1][1])

    def retornar_linha_smartprocess(self, linha):
        lista_users_to_create = self.carregar_ListaSmartProcess()
        return lista_users_to_create[linha]

    def registrar_log(self, data):
        try:
            filename = ("registro_logs.txt")

            with open(filename, 'a') as file_object:
                file_object.write("\n" + data)
        except BaseException as ex:
            print("Erro ao regisstrar_log {}".format(ex))
        finally:
            pass



class ActiveDirectory():
    def __init__(self):
        print("")

    def shortname(self):
        vbhost = win32com.client.Dispatch("ScriptControl")
        vbhost.language = "vbscript"
        vbhost.addcode("")



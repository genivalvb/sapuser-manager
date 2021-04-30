#!/usr/bin/env python3

from Ticket import *
from sap_user import *
from Geral import *
from db_dao_sap import *



class ControleTicket():
##==========================================================================
##==========================================================================
##==========================================================================
    def carregarListaUsers(self, dados, dadosSAP):
        geral = Geral()
        self.tickets = []
        self.tamanhoLista = len(dados)
        posicao = 1

        while posicao < self.tamanhoLista:
            self.ticket = Ticket()

            self.ticket.requestID = dados[posicao][0]
            self.ticket.systemType = dados[posicao][1]
            self.ticket.systemEnvironment = dados[posicao][2]
            self.ticket.plant = dados[posicao][3]
            self.ticket.tipoRequest = Ticket().tratarTipoRequest(dados[posicao][4])
            self.ticket.lastName = dados[posicao][6]
            self.ticket.name = dados[posicao][7]
            print("antes verificar se login existe")
            resultado = geral.verificarSeLoginExiste(dados[posicao][10], dadosSAP)
            if resultado != None:
                self.ticket.login = resultado
            else:
                self.ticket.login = self.definirLogin(self.ticket, geral, dadosSAP)

            self.ticket.function = dados[posicao][8]
            self.ticket.department = dados[posicao][9]
            self.ticket.email = dados[posicao][10]
            self.ticket.aliasUser = dados[posicao][11]
            #print(dados[posicao][69])
            #self.ticket.group = dados[posicao][69]
            self.ticket.language = dados[posicao][13]
            if dados[posicao][15] != "":
                self.ticket.departureDate = dados[posicao][15].replace("/",".").replace("-",".")


            self.ticket.sncName = "p:" + geral.getShortName(dados[posicao][10]) + "@VNET.VALEO.COM"
            self.ticket.sexo = "Sir"

            self.ticket.role01 = self.verifRole(dados[posicao][16])
            self.ticket.role02 = self.verifRole(dados[posicao][17])
            self.ticket.role03 = self.verifRole(dados[posicao][18])
            self.ticket.role04 = self.verifRole(dados[posicao][19])
            self.ticket.role05 = self.verifRole(dados[posicao][20])
            self.ticket.role06 = self.verifRole(dados[posicao][21])
            self.ticket.role07 = self.verifRole(dados[posicao][22])
            self.ticket.role08 = self.verifRole(dados[posicao][23])
            self.ticket.role09 = self.verifRole(dados[posicao][24])
            self.ticket.role10 = self.verifRole(dados[posicao][25])
            self.ticket.role11 = self.verifRole(dados[posicao][26])
            self.ticket.role12 = self.verifRole(dados[posicao][27])
            self.ticket.role13 = self.verifRole(dados[posicao][28])
            self.ticket.role14 = self.verifRole(dados[posicao][29])
            self.ticket.role15 = self.verifRole(dados[posicao][30])
            self.ticket.role16 = self.verifRole(dados[posicao][31])
            self.ticket.role17 = self.verifRole(dados[posicao][32])
            self.ticket.role18 = self.verifRole(dados[posicao][33])
            self.ticket.role19 = self.verifRole(dados[posicao][34])
            self.ticket.role20 = self.verifRole(dados[posicao][35])
            self.ticket.role21 = self.verifRole(dados[posicao][36])
            self.ticket.role22 = self.verifRole(dados[posicao][37])
            self.ticket.role23 = self.verifRole(dados[posicao][38])
            self.ticket.role24 = self.verifRole(dados[posicao][39])
            self.ticket.role25 = self.verifRole(dados[posicao][40])
            self.ticket.role26 = self.verifRole(dados[posicao][41])
            self.ticket.role27 = self.verifRole(dados[posicao][42])
            self.ticket.role28 = self.verifRole(dados[posicao][43])
            self.ticket.role29 = self.verifRole(dados[posicao][44])
            self.ticket.role30 = self.verifRole(dados[posicao][45])
            self.ticket.role31 = self.verifRole(dados[posicao][46])
            self.ticket.role32 = self.verifRole(dados[posicao][47])
            self.ticket.role33 = self.verifRole(dados[posicao][48])
            self.ticket.role34 = self.verifRole(dados[posicao][49])
            self.ticket.role35 = self.verifRole(dados[posicao][50])
            self.ticket.role36 = self.verifRole(dados[posicao][51])
            self.ticket.role37 = self.verifRole(dados[posicao][52])
            self.ticket.role38 = self.verifRole(dados[posicao][53])
            self.ticket.role39 = self.verifRole(dados[posicao][54])
            self.ticket.role40 = self.verifRole(dados[posicao][55])
            self.ticket.role41 = self.verifRole(dados[posicao][56])
            self.ticket.role42 = self.verifRole(dados[posicao][57])
            self.ticket.role43 = self.verifRole(dados[posicao][58])
            self.ticket.role44 = self.verifRole(dados[posicao][59])
            self.ticket.role45 = self.verifRole(dados[posicao][60])
            self.ticket.role46 = self.verifRole(dados[posicao][61])
            self.ticket.role47 = self.verifRole(dados[posicao][62])
            self.ticket.role48 = self.verifRole(dados[posicao][63])
            self.ticket.role49 = self.verifRole(dados[posicao][64])
            self.ticket.role50 = self.verifRole(dados[posicao][65])

            self.ticket.roleExceptional = self.verifRole(dados[posicao][66])
            self.ticket.roleExceptional1 = self.verifRole(dados[posicao][67])
            self.ticket.roleExceptional2 = self.verifRole(dados[posicao][68])
            self.ticket.group = dados[posicao][69]
            self.ticket.queries = str(dados[posicao][70:])

            self.tickets.append(self.ticket)
            posicao += 1


        return self.tickets


    def definirLogin(self, ticket, geral, dadosSAP):
        indice = 1
        resultado = None

        resultadoEmail = geral.verificarSeUserExiste(ticket.email,dadosSAP)

        if resultadoEmail == None:
            #print("ResultadoEmail = NONE")
            #resultado = "None"
            while resultado == None:
                loginMontado = geral.montarLogin(ticket.name, ticket.lastName, indice)
                resultadoLogin = geral.verificarSeLoginExiste(loginMontado, dadosSAP)
                #print("Indice antes de aumentar:" + str(indice))
                indice = indice + 1
                #print("Indice depois de aumentar:" + str(indice))
                #print("ResultadoLogin antes de testar" + str(resultadoLogin))
                if resultadoLogin == None:
                    resultado = loginMontado
                    break

        else:
            resultado = resultadoEmail


        return resultado

    def definir_login2(self, email):
        print(email)
        db_sap = DatabaseSap()
        print(email)
        print(db_sap.get_sap_login_if_email(email))
        #resultadoEmail = geral.verificarSeUserExiste(ticket.email, dadosSAP)




    @staticmethod
    def verifRole(role):
        if str(role[:9]) == "ZC_SFW_IMPORT":
            return str(role[:9])
        elif str(role[:13]) == "ZC_SFW_IMPORT":
            return str(role[:13])
        elif str(role[:18]) == "ZCR_NFEOUT_MONITOR":
            return str(role[:18])
        elif str(role[:17]) == "ZCR_NFEIN_MONITOR":
            return str(role[:17])
        else:
            return role
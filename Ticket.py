#!/usr/bin/env python3
from datetime import datetime


class Ticket():

    def __init__(self, requestID="", systemType="", systemEnvironment="", plant="", login="", lastName="", name=""
                 , function="", department="", email="", aliasUser="", group="", language="", departureData="31.12.9999"
                 , sncName="", sexo=""
                 ,role01="", role02="", role03="", role04="", role05="", role06="", role07="", role08="", role09=""
                 , role10="", role11="", role12="", role13="", role14="", role15="", role16="", role17="", role18=""
                 , role19="", role20="", role21="", role22="", role23="", role24="", role25="", role26="", role27=""
                 , role28="", role29="", role30="", role31="", role32="", role33="", role34="", role35="", role36=""
                 , role37="", role38="", role39="", role40="", role41="", role42="", role43="", role44="", role45=""
                 , role46="", role47="", role48="", role49="", role50="", roleExceptional="", roleExceptional1=""
                 , roleExceptional2="", orgaloc="",  queries="", tipoRequest="", existiu=0
                 , tipoUsuario=0, automatico=0, trip=0):
        self.requestID = requestID
        self.systemType = systemType
        self.systemEnvironment = systemEnvironment
        self.plant = plant
        self.login = login

        self.lastName = lastName
        self.name = name
        self.function = function
        self.department = department
        self.email = email
        self.aliasUser = aliasUser
        self.group = group
        self.language = language
        self.departureDate = self.tratarData(departureData)
        self.sncName = sncName
        self.sexo = sexo
        self.role01 = role01
        self.role02 = role02
        self.role03 = role03
        self.role04 = role04
        self.role05 = role05
        self.role06 = role06
        self.role07 = role07
        self.role08 = role08
        self.role09 = role09
        self.role10 = role10
        self.role11 = role11
        self.role12 = role12
        self.role13 = role13
        self.role14 = role14
        self.role15 = role15
        self.role16 = role16
        self.role17 = role17
        self.role18 = role18
        self.role19 = role19
        self.role20 = role20
        self.role21 = role21
        self.role22 = role22
        self.role23 = role23
        self.role24 = role24
        self.role25 = role25
        self.role26 = role26
        self.role27 = role27
        self.role28 = role28
        self.role29 = role29
        self.role30 = role30
        self.role31 = role31
        self.role32 = role32
        self.role33 = role33
        self.role34 = role34
        self.role35 = role35
        self.role36 = role36
        self.role37 = role37
        self.role38 = role38
        self.role39 = role39
        self.role40 = role40
        self.role41 = role41
        self.role42 = role42
        self.role43 = role43
        self.role44 = role44
        self.role45 = role45
        self.role46 = role46
        self.role47 = role47
        self.role48 = role48
        self.role49 = role49
        self.role50 = role50
        self.roleExceptional = roleExceptional
        self.roleExceptional1 = roleExceptional1
        self.roleExceptional2 = roleExceptional2
        self.orgaloc = orgaloc
        self.queries = queries
        self.tipoRequest = self.tratarTipoRequest(tipoRequest)
        self.existiu = existiu
        self.tipoUsuario = tipoUsuario
        self.automatico = automatico
        self.trip = trip
        #self.dateCreation = self.dataHoje()




    @staticmethod
    def tratarData(dados):
        data_departure = ""
        if len(dados):
            data_departure =dados.replace("/", ".")

            if data_departure[4] == ".":
                data_departure = data_departure[8:10] + "." + data_departure[5:7] + "." + data_departure[0:4]
        return data_departure


    @staticmethod
    def tratarTipoRequest(tipoRequest):
        #print("Tipo de Request: " + str(tipoRequest))
        if tipoRequest == "Create New User":
            return 0
        elif tipoRequest == "Change: add Job Profile/Plant":
            return 1
        elif tipoRequest == "Replace Job Profile":
            return 2
        elif tipoRequest == "Exceptional Access":
            return 3
        elif tipoRequest == "Delete User":
            return 4
        elif tipoRequest == "Unlock User":
            return 5
        else:
            return 6


    @staticmethod
    def verifRole(role):
        if str(role[:9]) == "ZC_SFW_IMPORT":
            return str(role[:9])
        elif str(role[:13])== "ZC_SFW_IMPORT":
            return str(role[:13])
        elif str(role[:18])== "ZCR_NFEOUT_MONITOR":
            return str(role[:18])
        elif str(role[:17])== "ZCR_NFEIN_MONITOR":
            return str(role[:17])
        else:
            return role

    @staticmethod
    def dataHoje(self):
        hoje = datetime.now()
        data = str(hoje.day) + "." + str(hoje.month) + "." + str(hoje.year)
        return data


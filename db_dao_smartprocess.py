import sqlite3
from Ticket import *
from Geral import *
from ControleTicket import *


class Database:
    def __init__(self, requestID="", systemType="", systemEnvironment="", plant="", login="", lastName="", name=""
                 , function="", department="", email="", aliasUser="", group="", language="", departureData="31.12.9999"
                 , sncName="", sexo=""
                 , role01="", role02="", role03="", role04="", role05="", role06="", role07="", role08="", role09=""
                 , role10="", role11="", role12="", role13="", role14="", role15="", role16="", role17="", role18=""
                 , role19="", role20="", role21="", role22="", role23="", role24="", role25="", role26="", role27=""
                 , role28="", role29="", role30="", role31="", role32="", role33="", role34="", role35="", role36=""
                 , role37="", role38="", role39="", role40="", role41="", role42="", role43="", role44="", role45=""
                 , role46="", role47="", role48="", role49="", role50="", roleExceptional="", roleExceptional1=""
                 , roleExceptional2="", queries="", tipoRequest="", existiu=0
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
        self.departureDate = departureData
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
        self.queries = queries
        self.tipoRequest = tipoRequest
        self.existiu = existiu
        self.tipoUsuario = tipoUsuario
        self.automatico = automatico
        self.trip = trip
        # self.dateCreation = self.dataHoje()

    @staticmethod
    def preencher_ticket(dados):
        tamanho = len(dados)
        dbdata = Database
        for i in range(tamanho):
            ticket = Ticket()
            geral = Geral()
            controleticket = ControleTicket()
            ticket.tipoRequest = dados[i][0]
            ticket.systemType = dados[i][1]
            ticket.systemEnvironment = dados[i][3]
            ticket.systemEnvironment = dados[i][2]
            ticket.plant = dados[i][3]
            ticket.tipoRequest = Ticket().tratarTipoRequest(dados[i][4])
            ticket.lastName = dados[i][6]
            ticket.name = dados[i][7]
            #resultado = geral.verificarSeLoginExiste(dados[][10], dadosSAP)
            ticket.function = dados[i][8]
            ticket.department = dados[i][9]
            ticket.email = dados[i][10]
            ticket.aliasUser = dados[i][11]
            ticket.language = dados[i][13]
            if dados[i][15] != "":
                ticket.departureDate = dados[i][15].replace("/", ".").replace("-", ".")

            ticket.sncName = "p:" + geral.getShortName(dados[i][10]) + "@VNET.VALEO.COM"
            ticket.sexo = "Sir"
            ticket.role01 = controleticket.verifRole(dados[i][16])
            ticket.role02 = controleticket.verifRole(dados[i][17])
            ticket.role03 = controleticket.verifRole(dados[i][18])
            ticket.role04 = controleticket.verifRole(dados[i][19])
            ticket.role05 = controleticket.verifRole(dados[i][20])
            ticket.role06 = controleticket.verifRole(dados[i][21])
            ticket.role07 = controleticket.verifRole(dados[i][22])
            ticket.role08 = controleticket.verifRole(dados[i][23])
            ticket.role09 = controleticket.verifRole(dados[i][24])
            ticket.role10 = controleticket.verifRole(dados[i][25])
            ticket.role11 = controleticket.verifRole(dados[i][26])
            ticket.role12 = controleticket.verifRole(dados[i][27])
            ticket.role13 = controleticket.verifRole(dados[i][28])
            ticket.role14 = controleticket.verifRole(dados[i][29])
            ticket.role15 = controleticket.verifRole(dados[i][30])
            ticket.role16 = controleticket.verifRole(dados[i][31])
            ticket.role17 = controleticket.verifRole(dados[i][32])
            ticket.role18 = controleticket.verifRole(dados[i][33])
            ticket.role19 = controleticket.verifRole(dados[i][34])
            ticket.role20 = controleticket.verifRole(dados[i][35])
            ticket.role21 = controleticket.verifRole(dados[i][36])
            ticket.role22 = controleticket.verifRole(dados[i][37])
            ticket.role23 = controleticket.verifRole(dados[i][38])
            ticket.role24 = controleticket.verifRole(dados[i][39])
            ticket.role25 = controleticket.verifRole(dados[i][40])
            ticket.role26 = controleticket.verifRole(dados[i][41])
            ticket.role27 = controleticket.verifRole(dados[i][42])
            ticket.role28 = controleticket.verifRole(dados[i][43])
            ticket.role29 = controleticket.verifRole(dados[i][44])
            ticket.role30 = controleticket.verifRole(dados[i][45])
            ticket.role31 = controleticket.verifRole(dados[i][46])
            ticket.role32 = controleticket.verifRole(dados[i][47])
            ticket.role33 = controleticket.verifRole(dados[i][48])
            ticket.role34 = controleticket.verifRole(dados[i][49])
            ticket.role35 = controleticket.verifRole(dados[i][50])
            ticket.role36 = controleticket.verifRole(dados[i][51])
            ticket.role37 = controleticket.verifRole(dados[i][52])
            ticket.role38 = controleticket.verifRole(dados[i][53])
            ticket.role39 = controleticket.verifRole(dados[i][54])
            ticket.role40 = controleticket.verifRole(dados[i][55])
            ticket.role41 = controleticket.verifRole(dados[i][56])
            ticket.role42 = controleticket.verifRole(dados[i][57])
            ticket.role43 = controleticket.verifRole(dados[i][58])
            ticket.role44 = controleticket.verifRole(dados[i][59])
            ticket.role45 = controleticket.verifRole(dados[i][60])
            ticket.role46 = controleticket.verifRole(dados[i][61])
            ticket.role47 = controleticket.verifRole(dados[i][62])
            ticket.role48 = controleticket.verifRole(dados[i][63])
            ticket.role49 = controleticket.verifRole(dados[i][64])
            ticket.role50 = controleticket.verifRole(dados[i][65])

            ticket.roleExceptional = controleticket.verifRole(dados[i][66])
            ticket.roleExceptional1 = controleticket.verifRole(dados[i][67])
            ticket.roleExceptional2 = controleticket.verifRole(dados[i][68])
            ticket.group = dados[i][69]
            ticket.queries = str(dados[i][70:])

        return ticket

    @staticmethod
    def insertdata(tickets):
        try:
            conn = sqlite3.connect('db\smartprocess.db')
            cursor = conn.cursor()
            #print("Connected to SQLITE")
            for ticket in tickets:
                insert_with_param = """INSERT INTO Tickets (request_id, system_type, system_environment, plant
                , type_request, sap_username, lastname, firstname, function, department, email, alias, user_group
                , language, timezone, departure_date, sncname, sexo, roles01, roles02, roles03, roles04, roles05, roles06
                , roles07, roles08, roles09, roles10, roles11, roles12, roles13, roles14, roles15, roles16, roles17
                , roles18, roles19, roles20, roles21, roles22, roles23, roles24, roles25, roles26, roles27, roles28
                , roles29, roles30, roles31, roles32, roles33, roles34, roles35, roles36, roles37, roles38, roles39
                , roles40, roles41, roles42, roles43, roles44, roles45, roles46, roles47, roles48, roles49, roles50
                , exceptional01, exceptional02, exceptional03, queries, existiu, tipousuario, automatico, trip)
                 VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?
                 ,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?
                 ,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);"""

                data_tuple = (ticket.requestID, ticket.systemType, ticket.systemEnvironment, ticket.plant, ticket.tipoRequest
                              ,ticket.login, ticket.lastName, ticket.name, ticket.function, ticket.department
                              , ticket.email, ticket.aliasUser, ticket.group, ticket.language, "timezone"
                              ,ticket.departureDate, ticket.sncName, ticket.sexo, ticket.role01, ticket.role02, ticket.role03, ticket.role04
                              , ticket.role05, ticket.role06, ticket.role07, ticket.role08, ticket.role09, ticket.role10
                              , ticket.role11, ticket.role12, ticket.role13, ticket.role14, ticket.role15, ticket.role16
                              , ticket.role17, ticket.role18, ticket.role19, ticket.role20, ticket.role21, ticket.role22
                              , ticket.role23, ticket.role24, ticket.role25, ticket.role26, ticket.role27, ticket.role28
                              , ticket.role29, ticket.role30, ticket.role31, ticket.role32, ticket.role33, ticket.role34
                              , ticket.role35, ticket.role36, ticket.role37, ticket.role38, ticket.role39, ticket.role40
                              , ticket.role41, ticket.role42, ticket.role43, ticket.role44, ticket.role45, ticket.role46
                              , ticket.role47, ticket.role48, ticket.role49, ticket.role50
                              , ticket.roleExceptional, ticket.roleExceptional1, ticket.roleExceptional2 ,ticket.orgaloc
                              ,str(ticket.queries), ticket.existiu
                              , ticket.tipoUsuario, ticket.automatico, ticket.trip)
                cursor.execute(insert_with_param, data_tuple)
                #print("Daremos o commit agora")
                conn.commit()

            #print("Tabela Tickets preenchida com sucesso")
            cursor.close()

        except sqlite3.Error as error:
            print("Failed to insert Python variable into sqlite table", error)
        finally:
            if (conn):
                conn.close()
                #print("The SQLite connection is closed")

    @staticmethod
    def reset_data():
        try:
            conn = sqlite3.connect('db\smartprocess.db')
            cursor = conn.cursor()
            #print("Connected to SQLite")

            sql_update_query = """UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='Tickets';"""
            cursor.execute(sql_update_query)
            conn.commit()
            #print("Record Updated successfully")
            cursor.close()
        except conn.Error as error:
            print("Failed to update sqlite table", error)
        finally:
            if(conn):
                conn.close()
                #print("The SQLite connection is closed")


    @staticmethod
    def insert_data_multiple(tickets):
        #print(tickets)
        try:
            conn = sqlite3.connect('db\smartprocess.db')
            cursor = conn.cursor()
            #print("Connected to SQLite")
            sqlite_insert_query = """INSERT INTO Tickets (request_id, system_type, system_environment, plant
                , type_request, sap_username, lastname, firstname, function, department, email, alias, user_group
                , language, timezone, departure_date, roles01, roles02, roles03, roles04, roles05, roles06
                , roles07, roles08, roles09, roles10, roles11, roles12, roles13, roles14, roles15, roles16, roles17
                , roles18, roles19, roles20, roles21, roles22, roles23, roles24, roles25, roles26, roles27, roles28
                , roles29, roles30, roles31, roles32, roles33, roles34, roles35, roles36, roles37, roles38, roles39
                , roles40, roles41, roles42, roles43, roles44, roles45, roles46, roles47, roles48, roles49, roles50
                , exceptional01, exceptional02, exceptional03, orgaloc, queries)
                 VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?
                 ,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?
                 ,?,?,?,?,?,?,?,?,?,?,?);"""
            #  sncname, sexo, existiu, tipousuario, automatico, trip
            #print('FERROU {}'.format(tickets))
            cursor.executemany(sqlite_insert_query, tickets)
            conn.commit()
            #print("Total", cursor.rowcount, "Records inserted successfully into SqliteDb_developers table")
            cursor.close()

        except sqlite3.Error as error:
            print("Failed to insert multiple records into sqlite table", error)
        finally:
            if (conn):
                conn.close()
                #print("The SQLite connection is closed")

    @staticmethod
    def get_ticket(id):
        try:
            conn = sqlite3.connect('db\smartprocess.db')
            cursor = conn.cursor()
            #print("Connected to SQLite")

            #sql_select_query = """SELECT * FROM Tickets where id = ? """
            sql_select_query = """SELECT * FROM Tickets where id = ? """
            cursor.execute(sql_select_query, (id,))
            registro = cursor.fetchone()
            #print("Record antes de fechar: ", registro[0])
            cursor.close()
            #print("Record depois de fechar: ", registro[1])
            return registro

        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if(conn):
                conn.close()
                #print("The SQLite connection is closed")

    @staticmethod
    def delete_data():
        try:
            conn = sqlite3.connect('db\smartprocess.db')
            cursor = conn.cursor()
            #print("Connected to SQLite")
            sqlite_update_query = """DELETE from Tickets;"""

            cursor.execute(sqlite_update_query)
            conn.commit()
            #print("Todas deletadas")
            cursor.close()
        except sqlite3.Error as error:
            print("Failed to delete multiple records from sqlite table", error)
        finally:
            if (conn):
                conn.close()
                #print("Sqlite connection is closed")

# insertVaribleIntoTable(2, 'Joe', 'joe@pynative.com', '2019-05-19', 9000)
# insertVaribleIntoTable(3, 'Ben', 'ben@pynative.com', '2019-02-23', 9500)
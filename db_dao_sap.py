import sqlite3
from Ticket import *
from Geral import *
from ControleTicket import *
from sap_user import sap_user


class DatabaseSap:
    def __init__(self, login="", email=""):
        self.login = login
        self.email = email
        # self.dateCreation = self.dataHoje()

    @staticmethod
    def preencher_ticket(dados):
        tamanho = len(dados)
        dbdata = DatabaseSap
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
    def insertdata(sap_user):
        try:
            conn = sqlite3.connect('db\sapusers.db')
            cursor = conn.cursor()
            #print("Connected to SQLITE")

            for user in sap_user:
                insert_with_param = """INSERT INTO sap_users (login, email)
                 VALUES(?,?);"""

                data_tuple = (sap_user.login , sap_user.email)
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
            conn = sqlite3.connect('db\sapusers.db')
            cursor = conn.cursor()
            #print("Connected to SQLite")

            sql_update_query = """UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='sap_users';"""
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
    def insert_data_multiple(sap_users):
        #print(sap_users)
        try:
            conn = sqlite3.connect('db\sapusers.db')
            cursor = conn.cursor()
            #print("Connected to SQLite")

            sqlite_insert_query = """INSERT INTO sap_users (login, email)
                 VALUES(?,?);"""
            #  sncname, sexo, existiu, tipousuario, automatico, trip

            cursor.executemany(sqlite_insert_query, sap_users)
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
    def get_sap_user_login(login):
        try:
            conn = sqlite3.connect('db\sapusers.db')
            cursor = conn.cursor()
            print("Connected to SQLite")

            sql_select_query = """SELECT login FROM sap_users where login = ? """
            cursor.execute(sql_select_query, (login,))
            registro = cursor.fetchone()
            print("Record antes de fechar: ", registro)
            cursor.close()
            print("Record depois de fechar: ", registro)
            return registro

        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if(conn):
                conn.close()
                print("The SQLite connection is closed")

    @staticmethod
    def get_sap_login_if_email(email):
        try:
            print("Genival002: {}".format(email))
            conn = sqlite3.connect('db\sapusers.db')
            cursor = conn.cursor()
            #print("DB Connected to SQLite login SAP")

            sql_select_query = """SELECT login FROM sap_users where email = ? """
            cursor.execute(sql_select_query, (email,))
            registro = cursor.fetchone()
            print("Record antes de fechar: ", registro)
            cursor.close()
            # print("Record depois de fechar: ", registro[1])
            return registro

        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if (conn):
                conn.close()
                print("The SQLite connection is closed")

    @staticmethod
    def delete_data():
        try:
            conn = sqlite3.connect('db\sapusers.db')
            cursor = conn.cursor()
            #print("Connected to SQLite")
            sqlite_update_query = """DELETE from sap_users;"""

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
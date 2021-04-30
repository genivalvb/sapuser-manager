import sqlite3
import Ticket

class Conflito():
    def __init__(self):
        a = 1 ## apenas para ter o _init__

    def conectarDB(self):
        global conn
        conn = sqlite3.connect('conflitos.db')
        global c
        c = conn.cursor()

    def fecharDB(self):
        global conn
        conn.close()

    def verificaConflito1(self, ticket, linha):
        self.conectarDB()
        role1 = ""
        role2 = ""
        role3 = ""
        #SQL
        sql1 = 'SELECT * FROM role1 where role = ?'
        sql2 = 'SELECT * FROM role2 where role = ?'
        sql3 = 'SELECT * FROM role1role2conflito where role1ID = ? AND role2ID = ?'
        sql4 = 'SELECT * FROM conflitos WHERE role1 = ? AND role2 = ? '
        sql5 = 'SELECT * FROM conflitos WHERE role2 = ? AND role1 = ? '

        if len(ticket.roleExceptional) > 0 and len(ticket.roleExceptional1)> 0:
            role1 = self.verificarBarra(ticket.roleExceptional)
            role2 = self.verificarBarra(ticket.roleExceptional1)
            print("ROLE1: %", role1)
            print("ROLE2: %", role2)
        elif len(ticket.roleExceptional1)> 0:
            role2 = self.verificarBarra(ticket.roleExceptional1)
            print("ROLE2: %", role2)
        elif len(ticket.roleExceptional2) > 0:
            role3 = self.verificarBarra(ticket.roleExceptional2)
            print("ROLE3: %", role3)
        else:
            return 99

        resultado = 5
        conflito = 5

        if len(role1) > 0 and len(role2) >0:
            print("Role01: %", role1)
            print("Role02: %", role2)
            conflito = self.read_data(role1, role2, sql4)

        self.fecharDB()

        #if conflito == 1 and linha == 1:
        #    conflito = 11
        #elif conflito == 1 and linha == 2:
        #    conflito = 12
        #elif conflito == 1 and linha == 3:
        #    conflito = 13

        return conflito


    def read_data(self,role1, role2, sql):
        global c
        for row in c.execute(sql, (role1, role2,)):
            print(row)
            return row[2]

    def read_data2(self, role1, role2):
        sql5 = 'SELECT * FROM conflitos WHERE role2 = ? AND role1 = ? '
        for row in c.execute(sql5, (role1, role2,)):
            print(row)

    def verificarBarra(self, role):
        if role[-5] == "_":
            resultado = role[:-5]
            print("Barra: %", resultado)
            return resultado
        elif role[-6] == "_":
            resultado = role[:-6]
            print("Barra: %", resultado)
            return resultado




#read_data("ZCR_AA_MST","ZCR_QUA_UTI")
#read_data2("ZCR_AA_MST","ZCR_ACC_TRE")

#conn.close()
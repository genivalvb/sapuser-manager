# _#_ coding: utf-8 _#_
"""
Criado em 11-03-2020 por Genival Silva
"""

import csv
import sqlite3
import sys

db_filename = "smartprocess.db"
data_filename = "smartprocess.csv"

SQL = """
insert into Tickets (request_id, system_type, system_environment, plant, type_request, sap_username,
lastname, firstname, function, department, email, alias, user_group, language, timezone, departure_date, 
roles01,roles02, roles03, roles04, roles05, roles06, roles07, roles08, roles09, roles10, roles11, roles12,
roles13, roles14, roles15, roles16, roles17, roles18, roles19, roles20, roles21, roles22, roles23, roles24,
roles25, roles26, roles27, exceptional01, exceptional02, exceptional03, orgaloc, queries) 
VALUES(%s,%s, %s,%s,%s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

with open(data_filename, 'rt') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with sqlite3.connect(db_filename) as conn:
        cursor = conn.cursor()
        cursor.executemany(SQL, csv_reader)



#values(:'Request ID',:'System Type', :'System Environment',:Plant,:'Type of Request', :'SAP Username',:'Last Name',
#:'First Name',:Function, :Department, :Email, :Alias, :'User Group', :Language, :TimeZone_ID, :'Departure Date',
#:Roles01, :Roles02, :Roles03, :Roles04, :Roles05, :Roles06, :Roles07, :Roles08 :Roles09, :Roles10, :Roles11,
#:Roles12, :Roles13, :Roles14, :Roles15, :Roles16, :Roles17, :Roles18, :Roles19, :Roles20, :Roles21, :Roles22,
#:Roles23, :Roles24, :Roles25, :Roles26, :Roles27, :'Exceptional Roles 01', :'Exceptional Roles 02', :'Exceptional Roles 03',
#:Orgaloc, :'Group of Queries Requested')
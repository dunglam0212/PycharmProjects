import mysql.connector

database = mysql.connector.connect(user='root', password='dungcute0212', host='localhost')
#QUERY
code = 'CREATE DATABASE `TEST1`'
#RUN
mycursor = database.cursor()
mycursor.execute(code)

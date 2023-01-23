#update python project
import mysql.connector
from admin import admin_register, admin_login
from user import user_register, user_login

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1seunwilliams!",
  database='project'
)
# # print(mydb)
mycursor = mydb.cursor()

# mydb = mysql.connector.connect(host = 'localhost', user = 'root', passwd = '1seunwilliams!' , database  = 'project')
# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE project")
# mycursor.execute("SHOW DATABASES")
# for database in mycursor:
#     print(database)

# table one
# sql = "DROP TABLE admin_table"
# mycursor.execute(sql)
# mycursor.execute("CREATE TABLE user_tab (Full_name VARCHAR(30), User_id INT(6), Password VARCHAR(20))")
# sql = 'DROP TABLE question'
# mycursor.execute(sql)
# mycursor.execute('CREATE TABLE admin_tab (Full_name VARCHAR(30), Admin_Id INT(6), password VARCHAR(20))')
# mycursor.execute("CREATE TABLE Question (question VARCHAR(100), option_a VARCHAR(30), option_b VARCHAR(30), option_c VARCHAR(30), answer VARCHAR(30))")
# mycursor.execute('ALTER TABLE Question. MODIFY COLUMN (question VARCHAR(100)) ')


opt = input(" 1. Admin 2. User\n")
if opt == '1':
    print('1. register 2. log in\n')
    optx = input(">>>")
    if optx == '2':
        admin_login.login()
    elif optx == '1':
        admin_register.register()

elif opt == '2':
    print('1. register 2. log in\n')
    opty = input('>>>')
    if opty == '1':
         user_register.register()
    elif opty =='2':
        user_login.login()
        
else:
    quit()

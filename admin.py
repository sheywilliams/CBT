import mysql.connector
mydb = mysql.connector.connect(host = 'localhost', user = 'root', passwd = '1seunwilliams!' , database  = 'project')
mycursor = mydb.cursor()
import numpy as np

# class admin:
#     def __init__(self):
#         self.login()
#     def login(self):
#         x = 0
#         while x <=3:
#              two = input('enter admin id\n>>>')
#              thr = input('enter pin\n >>>')
#              if two:
#                   myquery1 = 'SELECT * FROM admin_tab WHERE Admin_id=%s AND Password=%s'
#                   val1 = (two, thr)
#                   mycursor.execute(myquery1, val1)
#                   myreg = mycursor.fetchone()
#                   mydb.commit()
#                   print('Welcome Admin')
#     def question(self):

#                   question = input('Enter question\n>>>')
#                   option_a = input('Enter option a\n>>>')
#                   option_b = input('Enter option b\n>>>')
#                   option_c = input('Enter option c\n>>>') 
#                   answer = input('Enter correct answer\n>>>')
#                   myquery = 'INSERT INTO question (question, option_a, option_b, option_c, answer)  VALUES(%s, %s, %s, %s, %s)'
#                   val = (question, option_a, option_b, option_c, answer)
#                   mycursor.execute(myquery, val)
#                   mydb.commit()
#                   print(mycursor.rowcount, 'Question added successfully') 
#                   next = int(input('Enter 1 to continue or 2 to end.\n>>>'))
#                   if next == 1:
#                       admin.login()
#                   else:
#                       quit()
#              else:
#                   print('Try again, %d tries left' %(3-x)) 
#                   x += 1            
#         else:
#             print('Your account has been blocked')
#             # admin_login.login()
# # p = admin_login.login()
# # print(p)
# # admin_login.login() 





class admin_login:
    def __init__(self,nu):
        self.nu=nu
    def login():
              x = 0
              two = input('enter admin id\n>>>')
              thr = input('enter pin\n >>>')
            
              if two:
                  myquery1 = 'SELECT * FROM admin_tab WHERE Admin_id=%s AND Password=%s'
                  val1 = (two, thr)
                  mycursor.execute(myquery1, val1)
                  myreg = mycursor.fetchone()
                  mydb.commit()
                  print('Welcome Admin')
                  
                  question = input('Enter question\n>>>')
                  option_a = input('Enter option a\n>>>')
                  option_b = input('Enter option b\n>>>')
                  option_c = input('Enter option c\n>>>') 
                  answer = input('Enter correct answer\n>>>')
                  myquery = 'INSERT INTO question (question, option_a, option_b, option_c, answer)  VALUES(%s, %s, %s, %s, %s)'
                  val = (question, option_a, option_b, option_c, answer)
                  mycursor.execute(myquery, val)
                  mydb.commit()
                  print(mycursor.rowcount, 'Question added successfully') 
                  next = int(input('Enter 1 to continue or 2 to end.\n>>>'))
                  if next == 1:
                      admin_login.login()
                  else:
                      quit()
              else:
                   print('Wrong login details')
                   admin_login.login()        
# # m = admin_login()
# # m.login()                     

# # 
class admin_register:
    def __init__(self,nu):
        self.nu=nu
    def register():
        full_name = input('Enter full name\n>>>') 
        a_id = np.random.randint(1000, 1999)
        print('Your unique identification number is >>>')
        print(a_id)
        password = input('Enter password\n>>>') 

        myquery ='INSERT INTO admin_tab(Full_name, admin_id, password) VALUES (%s, %s, %s)'
        val = (full_name, a_id, password)
        mycursor.execute(myquery, val)
        mydb.commit()
        print(mycursor.rowcount, 'Admin added successfully') 

        next = int(input('Enter 1 to login or 2 to end.\n>>>'))
        if next == 1:
            admin_login.login()
        else:
            quit()
# # n = admin_register(1)
# # n.register()
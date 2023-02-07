import mysql.connector
mydb = mysql.connector.connect(host = 'localhost', user = 'root', passwd = '1seunwilliams!' , database  = 'project')
mycursor = mydb.cursor()
import pandas as pd
import numpy as np

class user_register:
    def __init__(self, nu):
        self.nu = nu
    def register():
         full_name = input('Enter full name\n') 
         u_id = np.random.randint(10000, 20000)
         print('Your unique identification number is >>>')
         print(u_id)
         password = input('Enter password\n') 

         myquery ='INSERT INTO user_tab(Full_name, user_id, password) VALUES (%s, %s, %s)'
         val = (full_name, u_id, password)
         mycursor.execute(myquery, val)
         mydb.commit()
         print(mycursor.rowcount, 'User added successfully') 

         next = int(input('Enter 1 to log in or 2 to end.\n'))
         if next == 1:
             user_login.login()
         else:
             quit()

class user_login:
    def __init__(self):
        self.login()
    def login(self):
        x = 0
        while x <= 3:
            user_id = input('enter user id >>>')
            pin = input('enter pin >>>')
            myquery1 = 'SELECT * FROM user_tab WHERE user_id=%s AND Password=%s'
            if user_id and pin in myquery1:
                print('Welcome User') 
                self.answer()
            else:
                print('Try again, %d tries left' %(3-x)) 
                x += 1  
            val1 = (user_id, pin)
            mycursor.execute(myquery1, val1)
            myreg = mycursor.fetchone()
            mydb.commit()
            
        else:
            print('Your account has been blocked')

        
#         # user_login.answer()
 
    def answer():
        score = 0
        enter = int(input('Select a question from numbers 1-10>>>'))
        query2 = "SELECT * FROM question WHERE question = %s"
        opt =(enter,)
        mycursor.execute(query2, opt)
        fetch = mycursor.fetchone()
        mydb.commit()
        if 'enter' in query2:
            print(fetch.loc[0])
            print('(a)', fetch[2])
            print('(b)', fetch[3])
            print('(c)', fetch[4])

            answer = input('Enter answer')
            query = "SELECT * FROM question WHERE answer = %s"
            val = (answer,)
            mycursor.execute(query, val)
            select = mycursor.fetchone()
            try:
                if answer in select:
                    score += 1
                    print('correct')
            except:
                print('wrong')
            else:
                quit()

# class user_login:
#     def __init__(self, nu):
#         self.nu = nu
#     def login():
#         user_id = input('enter user id >>>')
#         pin = input('enter pin >>>')
#         try:
#              res = re.search(r"\b@.\w+", user_id)
#              if res.string in user_id:
#                  query = "SELECT user_id, Full_name, WHERE user_id=%s AND pin=%s"
#                  value = (user_id, pin)
#                  mycursor.execute(query, value)
#                  myreg = mycursor.fetchone()
#                  print(myreg)
#                  try:
#                       if myreg[2] == user_id:
#                           user_login.question()
#                  except TypeError:
#                          pass
#              else:
#                  print('Invalid user_id...Retry')
        
    # def question():
    #      score = 0
    #      for x in range(3):
    #          select = int(input('Enter any number from 1 to 10:'))
    #          query_one = "SELECT * FROM question WHERE user_id = %s"
    #          value = (select,)
    #          mycursor.execute(query_one, value)
    #          fetch = mycursor.fetchone()
    #      try:
    #          if fetch[0] == select:
    #              print(fetch[1])
    #              print('(a)', fetch[2])                            
    #              print('(b)', fetch[3])                            
    #              print('(c)', fetch [4])

    #              pick = input('Enter answer')
    #              query = "SELECT * FROM question WHERE answer = %s"
    #              value = (pick,)
    #              mycursor.execute(query,value)
    #              nm = mycursor.fetchone()
    #              try:
    #                  if pick in nm:
    #                      score += 1
    #                      print('Correct', 'You have',score, 'point')

    #              except TypeError:
    #                  score 
    #                  print('Incorrect', 'you have',score,'point')

    #      except TypeError:
    #          print('Number not inside...Retry')  







    # def login():
    #           two = input('Enter user id\n >>>')
    #           thr = input('Enter pin\n >>>')
    #           myquery1 = 'SELECT * FROM user_tab WHERE user_id=%s AND Password=%s'
    #           val1 = (two, thr)
    #           mycursor.execute(myquery1, val1)
    #           myreg = mycursor.fetchone()
    #           mydb.commit()
    #           print('Welcome User') 
    #           self.answer()
    # def answer():
    #     try:
    #         score = 0
    #         while True:
    #             enter = int(input('Select a question from numbers 1-10>>>'))
    #             query1 = "SELECT * FROM question WHERE user_id = %s"
    #             opt =(enter,)
    #             mycursor.execute(query1, opt)
    #             xo = mycursor.fetchone()
    #             try:
    #                 if xo[0] == enter:
    #                     print(xo[1])
    #                     print('(a)', xo[2])
    #                     print('(b)', xo[3])
    #                     print('(c)', xo[4])

    #                     pick = input('Enter answer')
    #                     query = "SELECT * FROM question WHERE answer = %s"
    #                     val = (pick,)
    #                     mycursor.execute(query, val)
    #                     ox = mycursor.fetchone()
    #                     try:
    #                         if pick in ox:
    #                             score += 1
    #                             print('correct')
    #                     except:
    #                        print('wrong')
                    #   else:
                    #       quit()
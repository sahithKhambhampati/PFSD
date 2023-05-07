import psycopg2
conn = psycopg2.connect(
    database="sahith", user='postgres',
    password='@Sahith@123',
    host='127.0.0.1', port='5432'
)

cursor = conn.cursor()

sql = '''CREATE TABLE P1111(
     yourname CHAR(20) NOT NULL,
     Message char(500)
     )'''
cursor.execute(sql)
print("Table created successfully......")
print("Records inserted......")
cursor.execute('''INSERT INTO P1111(yourname,Message) VALUES ('Sahith12','Why is project management important?')''')
cursor.execute('''INSERT INTO P1111(yourname,Message) VALUES ('abc','What is the best project management software for small businesses?')''')
cursor.execute('''INSERT INTO P1111(yourname,Message) VALUES ('Sss','What are the three main types of project management software?')''')
cursor.execute('''INSERT INTO P1111(yourname,Message) VALUES ('Sah12','What are the benefits of project management software?')''')
cursor.execute('''INSERT INTO P1111(yourname,Message) VALUES ('Sa','What are the different types of project management methods that are popular now?')''')


conn.commit()

# sql1='''UPDATE STUDENT0 SET NAME='lehan',AGE='19' WHERE REGNUM=30252'''
# cursor.execute(sql1)
# print("updated")

# sql2='''SELECT *FROM STUDENT'''
# cursor.execute(sql2)
# print(cursor.fetchall())

# sql3 = '''DROP TABLE STUDENT'''
# cursor.execute(sql3)
# print("table dropped successfully")

conn.commit()

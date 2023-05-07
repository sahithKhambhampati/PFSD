import psycopg2
conn = psycopg2.connect(
    database="sahith", user='postgres',
    password='@Sahith@123',
    host='127.0.0.1', port='5432'
)

cursor = conn.cursor()

sql = '''CREATE TABLE PJS1(
     USERNAME CHAR(20) NOT NULL,
     PASSWORD char(10)
     )'''
cursor.execute(sql)
print("Table created successfully......")
print("Records inserted......")
cursor.execute('''INSERT INTO PJS1(USERNAME,PASSWORD) VALUES ('Sahith12',12345)''')
cursor.execute('''INSERT INTO PJS1(USERNAME,PASSWORD) VALUES ('bunny',30033)''')
cursor.execute('''INSERT INTO PJS1(USERNAME,PASSWORD) VALUES ('Sreeja',30258)''')
cursor.execute('''INSERT INTO PJS1(USERNAME,PASSWORD) VALUES ('abcd',1234)''')
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

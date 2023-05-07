import psycopg2
conn = psycopg2.connect(
    database="sahith", user='postgres',
    password='@Sahith@123',
    host='127.0.0.1', port='5432'
)

cursor = conn.cursor()

sql = '''CREATE TABLE PJ111(
     YourName CHAR(20) NOT NULL,
     ProjectName char(10),
     SpecialstName CHAR(20) NOT NULL,
     YourEmail CHAR(50),
     dd_mm_yyyy CHAR(15)
     )'''
cursor.execute(sql)
print("Table created successfully......")
print("Records inserted......")
cursor.execute('''INSERT INTO PJ111(YourName,ProjectName,SpecialstName,YourEmail,dd_mm_yyyy) VALUES ('Sahith','Farming','Varshith','sahithkhambhampati@gmail.com',12-04-2023)''')
cursor.execute('''INSERT INTO PJ111(YourName,ProjectName,SpecialstName,YourEmail,dd_mm_yyyy) VALUES ('Sreeja','School','rishitha','sreejakodumuru2003@gmail.com',14-05-2023)''')
cursor.execute('''INSERT INTO PJ111(YourName,ProjectName,SpecialstName,YourEmail,dd_mm_yyyy) VALUES ('Bunny','Event','Charan','charan17@gmail.com',16-04-2023)''')
cursor.execute('''INSERT INTO PJ111(YourName,ProjectName,SpecialstName,YourEmail,dd_mm_yyyy) VALUES ('Sriram','Banking','Akhila','sriram2004@gmail.com',2-07-2023)''')
conn.commit()

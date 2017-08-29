import pymysql

conn= pymysql.connect(host='localhost', user='root', password='rtyhnbvfg', db='qwerty')

a=conn.cursor()

sql= 'SELECT * FROM `users`;'

a.execute(sql)

countrow = a.execute(sql)

print 'count of row', countrow

data = a.fetchall()
print 'data is ', data

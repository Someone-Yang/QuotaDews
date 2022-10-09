import sqlite3

sqlcon = sqlite3.connect('./example.db')
print ("连接到数据库")
sqlcur = sqlcon.cursor()
icur = sqlcur.execute("SELECT ID,CONTENT,AUTHOR,CATEGORY,CREATED from QUOTADEWS")
for row in icur:
   print ("[", row[0],"]")
   print ("伟大的", row[2],"说：")
   print (row[1])
   print ("[创建时间", row[4], "]\n")
sqlcon.commit()
sqlcur.close()
sqlcon.close()
print ("关闭数据库")
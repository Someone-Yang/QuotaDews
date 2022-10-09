# 语露数据库初始化工具
import sqlite3

sqlcon = sqlite3.connect('./example.db')
print ("连接到数据库")
sqlcur = sqlcon.cursor()
sqlcur.execute('''CREATE TABLE QUOTADEWS
       (ID INT PRIMARY KEY    NOT NULL,
       CONTENT        TEXT     NOT NULL,
       AUTHOR         CHAR(50)     NOT NULL,
       CATEGORY       INT,
       CREATED        CHAR(20));''')
print ("创建数据表完成")
sqlcon.commit()
sqlcur.close()
sqlcon.close()
print ("关闭数据库")
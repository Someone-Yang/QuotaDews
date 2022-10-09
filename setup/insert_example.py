from datetime import datetime
import sqlite3

def insert (iCur,iContent,iAuthor,iCategory):
  iCur.execute ("SELECT * FROM QUOTADEWS")
  iRows = len(iCur.fetchall())
  print ("[认为数据库长度为" + str(iRows) + "]")
  iCur.execute("INSERT INTO QUOTADEWS (ID,CONTENT,AUTHOR,CATEGORY,CREATED) \
      VALUES ("+str(iRows + 1)+", '"+iContent+"', '"+iAuthor+"', "+str(iCategory)+", '"+str(datetime.now())+"' )")
  print ("[插入一条数据]" + iContent + " - By " + iAuthor)

sqlcon = sqlite3.connect('./example.db')
print ("连接到数据库")
sqlcur = sqlcon.cursor()
insert (sqlcur,"逸一时误一世，逸久逸久罢已龄。","田所浩二",1)
insert (sqlcur,"喂，卖唱的，你不要太过分！我没发现什么？明明连丘丘人、野猪都打不过，气势却比谁都嚣张。","派蒙",1)
insert (sqlcur,"可莉不知道哦","可莉",1)
insert (sqlcur,"这么厉害","Simon",1)
insert (sqlcur,"当你重新踏上旅途之后,一定要记得旅途本身的意义。","温迪",1)
insert (sqlcur,"飘摇风雨中，睹物思故乡。","枫原万叶",1)
sqlcon.commit()
sqlcur.close()
sqlcon.close()
print ("关闭数据库")
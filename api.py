import random
import flask,json,sqlite3

qdapi = flask.Flask(__name__)

@qdapi.route('/quotadews',methods=['get'])
def quotadews():
  # 连接数据库
  sqlcon = sqlite3.connect('./example.db')
  print ("连接到数据库")
  sqlcur = sqlcon.cursor()
  # 获取所有数据
  sqlcur.execute ("SELECT * FROM QUOTADEWS")
  iRows = sqlcur.fetchall()
  # 找到最大行数
  iRowMount = len(iRows)
  print ("[认为数据库长度为" + str(iRowMount) + "]")
  # 随机列表项
  iRandom = random.randint (0,iRowMount - 1)
  print ("认为随机数列表项是("+str(iRandom)+")，数据库第("+str(iRandom + 1)+")行")
  # 准备返回信息
  ren = {"status":"1","quotadew":{
    "id":iRows[iRandom][0],
    "content":iRows[iRandom][1],
    "author":iRows[iRandom][2],
    "category":iRows[iRandom][3],
    "created":iRows[iRandom][4]
    }
  }
  # 以 json 返回数据
  return (json.dumps(ren,ensure_ascii=False),200)

if __name__ == '__main__':
  qdapi.run(port=8888,debug=True,host='127.0.0.1')
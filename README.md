# 语露 / QuotaDews

> Python 个人学习项目，无实际生产使用意义.jpeg

## 创建数据库

使用 SQLite 数据库。在目录`/setup`中，首先运行`setup_sqilite.py`来创建结构的 SQLite 数据库文件。将在项目目录生成 `example.db` 示例数据库。然后，可以运行 `insert_example.py` 来插入一些示例数据。最后，可以使用 `viewdata.py` 列出数据。

|表头|类型|备注|
|---|---|---|
|ID|INT PRIMARY KEY|非空|
|CONTENT|TEXT|语句内容|
|AUTHOR|CHAR(50)|作者或出处|
|CATEGORY|INT|分类|
|CREATED|CHAR(20)|如果不出意外，是创建时间。|

那几坨字段暂时没想好到底该怎么处理。但是留着肯定没问题。

## 跑起api

同目录运行 `api.py` ，访问 `http://127.0.0.1:8888/quotadews` 就可以玩了。
##### 1.python连接MySQL
```python
import pymysql
from pymysql import connect

hostname = '127.0.0.1'
port = 3306
user = 'root'
passwd = '5683'
db = 'mimiciiiv14'
conn = connect(host=hostname, port=port, user=user, passwd=passwd, db=db)
cursor = conn.cursor()

sql = 'SELECT * FROM admissions WHERE DIAGNOSIS LIKE \'%PNEUMONIA%\''

num = cursor.execute(sql) ## 一条一条查询
num = cursor.executemany(sql)   ## 多条查询
print(num) ## 显示多少条记录
all_match = cursor.fetchall() ## 返回元组

## 将查询的记录放入DataFrame中
admissions_df_full = pd.read_sql_query(sql, conn)

```
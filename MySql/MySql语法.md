##### 1.给已有的**test表**添加一个自增的序列并设置为主键，该列名为**id**：
```mysql
alter table test add id int auto_increment primary key;
```

##### 2.将某列col_name设置为主键：
```mysql
alter table table_name add primary key (col_name);
```

##### 3.mysql数据库将文件内容加载到数据表中，出现以下错误：
```mysql
ERROR 1148: The used command is not allowed with this MySQL version
或者
Loading local data is disabled; this must be enabled on both the client and
```
**解决办法：**
首先进去mysql（用户名为root）
```mysql
mysql -u root -p 
show variables like '%local%';
```
然后得到local_infile OFF 即该变量未开启，将该变量设置为ON，即可；
![image-20200508160652570](C:\Users\yu_zh\AppData\Roaming\Typora\typora-user-images\image-20200508160652570.png)

```mysql
set global local_infile=1;
```
![image-20200508160707340](C:\Users\yu_zh\AppData\Roaming\Typora\typora-user-images\image-20200508160707340.png)

然后退出mysql数据库，重新使用以下命令进入：
```mysql
mysql -u root -p --local-infile=1
```
##### 4.执行mysql脚本文件
进入mysql控制台
```mysql
\. file.sql 或 source C:\file.sql
```
##### 5.删除数据表test中的idx列
```mysql
ALTER TABLE test DROP COLUMN  idx;
```
##### 6.清空数据表test中的所有记录，并保留数据表结构
```mysql
TRUNCATE TABLE test;
```
##### 7.彻底删除数据表test
```mysql
drop TABLE test;
```
##### 8.创建数据表test，并设置id为自增的主键
```mysql
CREATE TABLE test(
id int PRIMARY KEY AUTO_INCREMENT,
pmid VARCHAR(255)
);
--插入数据
insert into test values (null,'111');
```
##### 9.修改数据表中的名称，列名以及类型
```mysql
-- 修改表名 
rename table old_table to new_table;

-- 或者
alter table old_table rename as new_table;

-- 修改列名称
alter table table_name change column old_name new_name varchar(255);

-- 修改字段类型
alter table table_name modify column column_name varchar(255) default '' COMMENT '注释';
```

数据表：

table name prima 
col1 col2 col3 col4 col5
aa1 bb1 cc1 dd1 ee1   *
aa1 bb1 cc1 dd1 ee1   *
aa1 bb1 cc2 dd4 ee4   %
aa2 bb2 cc2 dd2 ee2   #
aa3 bb3 cc3 dd3 ee3   $
aa3 bb3 cc3 dd3 ee3   $
aa3 bb3 cc3 dd3 ee3   $

```mysql
1、增加一列自动增长的id:
alter table prima add id int auto_increment primary key;
2、删除重复数据，只保留一条记录:
delete from prima using (prima,(select distinct min(id) as id ,col1,col2,col3 from prima group by col1,col2,col3 having count(1)>1) as t2 ) where prima.col1=t2.col1 and prima.col2=t2.col2 and prima.col3=t2.col3 and prima.id > t2.id;
3、删除id字段:
alter table prima drop id;
```
启动mysql服务，可以查看错误日志
```mysql
mysqld --console
```
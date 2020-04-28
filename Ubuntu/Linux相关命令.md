# 服务器相关命令

#### 1.将程序放在后台进行运行：
```
nohup python test.py &
```
#### 2.使用下面命令可以查看正在输出的nohup.out文件的内容，并实时查看程序的运行情况。
```python
tail -fn 50 nohup.out
```
#### 3.查看服务器显卡使用情况
```python
nvidia-smi
```
#### 4.查看服务器运行中系统的动态实时视图
```python
top
```
#### 5.删除文件或文件夹
```python
rm -f dir
```
#### 6.复制文件夹(将dir_old文件复制到dir_new中)
```python
cp dir_old dir_new
## 移动所有文件夹里的所有文件
cp dir_old/* dir_new
```
#### 7.将anaconda环境共享使其它用户也可以使用
##### 1）查看 /etc/profile里面有没有export 的语句，如果没有则运行
```
export PATH=/anaconda的路径/bin:$PATH
```

##### 2）将root和其他用户放在同一个共享组下面，创建新的用户组 anaconda可以改为想设的组名
```
sudo groupadd anaconda
```
##### 3）把Anaconda安装的整个文件夹的组的拥有者设为刚才创建的组名
```
 sudo chgrp -R anaconda /opt/anaconda3(anaconda的安装目录)
```
 #### 4.修改安装的文件夹的权限
```
sudo chmod 770 -R /opt/anaconda3(anaconda的安装目录) 
```
#### 5.把用户添加进组  
```
 sudo usermod –a username -G anaconda (G为用户名）
 ```
 
#### 6.解压7z，zip，rar等压缩包
```
#安装7z
sudo apt-get install p7zip
7z a test.7z  # 压缩为7z
7z x test.7z  #解压

unzip test.zip  #解压
```




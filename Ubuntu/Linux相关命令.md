# 服务器相关命令

#### 1.将程序放在后台进行运行：
```
nohup python test.py &

nohup python -u text.py > log.txt 2>&1 &
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
 ##### 4).修改安装的文件夹的权限
```
sudo chmod 770 -R /opt/anaconda3(anaconda的安装目录) 
```
##### 5).把用户添加进组  
```
 sudo usermod –a username -G anaconda (G为用户名）
```



#### 8.解压7z，zip，rar等压缩包

```
#安装7z
sudo apt-get install p7zip
7z a test.7z  # 压缩为7z
7z x test.7z  #解压

unzip test.zip  #解压
```



#### 9. 安装和卸载程序

##### 9.1 安装程序

1）去官网下载安装包，然后解压安装包，并移动到/opt目录下（移到到opt目录下是为了让所有用户都能够使用该程序）

```
Tar –zxvf name.tar.gz
```

2）配置文件目录

启动该程序，会在用户的家目录下建立一个.name的隐藏目录（.name为该程序名）；保存相关配置信息

```
Sudo mv name/ /opt

Cd /opt/name/bin

./name
```

3）快捷方式文件

在Ubuntu中，应用程序启动的快捷方式通常都保存在`/usr/share/applications/`下

##### 9.2 卸载程序

1）删除解压缩目录

````
sudo rm –r /opt/name  （name为要删除的程序）
````

2）删除家目录下用户保存配置信息的隐藏目录

```
sudo rm –r ~/.name/     （name为删除的程序的目录）
```

3）删除桌面下的快捷方式（在/usr/share/applications/下）

```
sudo rm -r /usr/share/applications/name.desktop  (name为快捷方式的名字)
```



#### 10.scp远程传输文件

```
# 把本地copy到远程服务器上
scp 文件相对路径 远程主机用户名@主机ip:传输到远程主机的相对路径
scp /data/test.py root@10.0.30.3:/data/user

# 把远程服务器的文件copy到本地
scp 远程主机用户名@主机ip:文件相对路径 传输到本地的相对路径
scp root@10.0.30.3:/data/test.py /data/user

## 如果需要传输整个文件夹，则在scp后面加 -r
scp -r /data/test.py root@10.0.30.3:/data/user
```


#### 11.开启root用户

```
sudo passwd root
```

#### 12.配置Zsh

##### 1）安装Zsh

~~~
# 安装Zsh
sudo apt-get install zsh

# 将Zsh设置为默认Shell
chsh -s /bin/zsh

# 将bash设置为默认Shell
chsh -s /bin/bash
~~~

##### 2）安装Oh My Zsh

~~~
# 安装 Oh My Zsh
wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | sh
# 以上命令可能不好使，可使用如下两条命令
wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh
bash ./install.sh
~~~

##### 3)安装zsh-syntax-highlighting

```
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```

##### 4)安装zsh-autosuggestions

```
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
```

##### 5)将anaconda环境加入zsh中

```
# 1)打开~/.bashrc

__conda_setup="$('/data/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
        eval "$__conda_setup"
else
        if [ -f "/data/anaconda3/etc/profile.d/conda.sh" ]; then
                . "/data/anaconda3/etc/profile.d/conda.sh"
        else
                export PATH="/data/anaconda3/bin:$PATH"
        fi
fi
unset __conda_setup

将上面conda的配置复制到~/.zshrc当中
```




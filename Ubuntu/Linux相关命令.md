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

#### 13.tmux的安装与使用

```
## 安装
sudo apt-get install tmux

## 新建终端
tmux new -s test(会话名称)

## 进入终端
tmux a -t test(会话名称)

## 列出所有会话
tmux ls

## 关闭会话
tmux kill-session -t test(会话名称)
```

注意：

```
1）进入tmux面板后，一定要先按ctrl+b，然后松开，再按其他的组合键才生效。
 
2）常用到的几个组合键：
ctrl+b ?            显示快捷键帮助
ctrl+b 空格键       采用下一个内置布局，这个很有意思，在多屏时，用这个就会将多有屏幕竖着展示
ctrl+b !            把当前窗口变为新窗口
ctrl+b  "           模向分隔窗口
ctrl+b %            纵向分隔窗口
ctrl+b q            显示分隔窗口的编号
ctrl+b o            跳到下一个分隔窗口。多屏之间的切换
ctrl+b 上下键      上一个及下一个分隔窗口
ctrl+b C-方向键    调整分隔窗口大小
ctrl+b &           确认后退出当前tmux
ctrl+b [           复制模式，即将当前屏幕移到上一个的位置上，其他所有窗口都向前移动一个。
ctrl+b c           创建新窗口
ctrl+b n           选择下一个窗口
ctrl+b l           最后使用的窗口
ctrl+b p           选择前一个窗口
ctrl+b w           以菜单方式显示及选择窗口
ctrl+b s           以菜单方式显示和选择会话。这个常用到，可以选择进入哪个tmux
ctrl+b t           显示时钟。然后按enter键后就会恢复到shell终端状态
ctrl+b d           脱离当前会话；这样可以暂时返回Shell界面，输入tmux attach能够重新进入之前的会话
```

###### 系统操作

| ?      | 列出所有快捷键；按q返回                                      |
| ------ | ------------------------------------------------------------ |
| d      | 脱离当前会话；这样可以暂时返回Shell界面，输入tmux attach能够重新进入之前的会话 |
| D      | 选择要脱离的会话；在同时开启了多个会话时使用                 |
| Ctrl+z | 挂起当前会话                                                 |
| r      | 强制重绘未脱离的会话                                         |
| s      | 选择并切换会话；在同时开启了多个会话时使用                   |
| :      | 进入命令行模式；此时可以输入支持的命令，例如kill-server可以关闭服务器 |
| [      | 进入复制模式；此时的操作与vi/emacs相同，按q/Esc退出          |
| ~      | 列出提示信息缓存；其中包含了之前tmux返回的各种提示信息       |

###### 窗口操作

| c      | 创建新窗口                           |
| ------ | ------------------------------------ |
| &      | 关闭当前窗口                         |
| 数字键 | 切换至指定窗口                       |
| p      | 切换至上一窗口                       |
| n      | 切换至下一窗口                       |
| l      | 在前后两个窗口间互相切换             |
| w      | 通过窗口列表切换窗口                 |
| ,      | 重命名当前窗口；这样便于识别         |
| .      | 修改当前窗口编号；相当于窗口重新排序 |
| f      | 在所有窗口中查找指定文本             |

###### 面板操作

| ”           | 将当前面板平分为上下两块                                     |
| ----------- | ------------------------------------------------------------ |
| %           | 将当前面板平分为左右两块                                     |
| x           | 关闭当前面板                                                 |
| !           | 将当前面板置于新窗口；即新建一个窗口，其中仅包含当前面板     |
| Ctrl+方向键 | 以1个单元格为单位移动边缘以调整当前面板大小                  |
| Alt+方向键  | 以5个单元格为单位移动边缘以调整当前面板大小                  |
| Space       | 在预置的面板布局中循环切换；依次包括even-horizontal、even-vertical、main-horizontal、main-vertical、tiled |
| q           | 显示面板编号                                                 |
| o           | 在当前窗口中选择下一面板                                     |
| 方向键      | 移动光标以选择面板                                           |
| {           | 向前置换当前面板                                             |
| }           | 向后置换当前面板                                             |
| Alt+o       | 逆时针旋转当前窗口的面板                                     |
| Ctrl+o      | 顺时针旋转当前窗口的面板                                     |

14. 杀死username下的所有进程

```
killall -u username
```




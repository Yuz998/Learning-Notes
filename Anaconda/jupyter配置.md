# 一、更换工作目录

打开`C:\Users\yu_zh\.jupyter\jupyter_notebook_config.py`

搜索`c.NotebookApp.notebook_dir`

```python
c.NotebookApp.notebook_dir = 'D:\JupyterNotebook'
```

# 二、更换浏览器

搜索`c.NotebookApp.browser`

添加下面代码

```python
import webbrowser
webbrowser.register('chrome', None, webbrowser.GenericBrowser(u'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'))
c.NotebookApp.browser = 'chrome'
```

# 三、更换主题

下载`jupyterthemes`模块

```python
pip install jupyterthemes
```

查看主题名称

```python
jt -l
```

```
jt -t grade3 -cellw 96% -T -N -fs 12 -tfs 13 -nfs 13 -altp
```



当前主题` grade3`

![image-20200818104727166](C:\Users\yu_zh\AppData\Roaming\Typora\typora-user-images\image-20200818104727166.png)

# 四、插件安装

https://zhuanlan.zhihu.com/p/97394628

```python
pip install jupyter_nbextensions_configurator
jupyter nbextensions_configurator enable --user
```

![image-20200818120126126](C:\Users\yu_zh\AppData\Roaming\Typora\typora-user-images\image-20200818120126126.png)


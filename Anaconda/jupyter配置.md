# 一、更换工作目录

(windows下)打开`C:\Users\yu_zh\.jupyter\jupyter_notebook_config.py`
(Linux和Linux子系统) 打开 `/home/users/.jupyter/jupyter_notebook_config.py` (运行 jupyter notebook --generate-config 产生jupyter_notebook_config.py文件)

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
jt -t grade3 -cellw 96% -T -N -fs 14 -tfs 14 -nfs 14 -ofs 14
```



当前主题` grade3`

![image-20200818104727166](C:\Users\yu_zh\AppData\Roaming\Typora\typora-user-images\image-20200818104727166.png)

# 四、插件安装

https://zhuanlan.zhihu.com/p/97394628

```python
pip install jupyter_nbextensions_configurator
jupyter nbextensions_configurator enable --user

pip install -i http://pypi.douban.com/simple --trusted-host pypi.douban.com jupyter_contrib_nbextensions

jupyter contrib nbextension install --user


pip install -i http://pypi.douban.com/simple --trusted-host pypi.douban.com  jupyter_nbextensions_configurator

jupyter nbextensions_configurator enable --user

```
https://www.cnblogs.com/qiuxirufeng/p/9609031.html

![image-20200818120126126](C:\Users\yu_zh\AppData\Roaming\Typora\typora-user-images\image-20200818120126126.png)


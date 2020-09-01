# Anaconda配置R语言

```
conda install r
```



# 一、R语言的安装与运行（Vscode + R.exe）

## 1）R的安装

R语言的安装：https://cran.r-project.org/

![image-20200818003128903](C:\Users\yu_zh\AppData\Roaming\Typora\typora-user-images\image-20200818003128903.png)

Windows：https://cran.r-project.org/bin/windows/base/

MAC：https://cran.r-project.org/

Linux：https://cran.r-project.org/src/base/R-4/

```R
sudo apt -y install r-base
```

## 2）Vscode安装R插件

只需要按照`R language support` 和`R LSP Client`即可

![image-20200818003109021](C:\Users\yu_zh\AppData\Roaming\Typora\typora-user-images\image-20200818003109021.png)

![image-20200818003055629](C:\Users\yu_zh\AppData\Roaming\Typora\typora-user-images\image-20200818003055629.png)



## 3）R语言的运行

### 3.1 在终端运行

```R
Rscript test.R
```

## 3.2在Vscode里运行

点击右上角中间的运行按钮即可



# 二、R依赖包的安装和加载

```R
## 安装依赖包
install.packages('ggplot2')
## 加载依赖包
library(ggplot2)
## 更新依赖包
update.packages()

## 更换镜像源
chooseCRANmirror()
```

# 三、R语言基础

```R
## 创建一个向量：
vec = c(1, 4, 4, 3, 2, 2, 3) # 下标从1开始

## 返回向量中的元素
vec[c(2, 3, 4)] ## 取下标为2， 3， 4的元素
# out：4 4 3
vec[2:4]   ## 取下标从2到4的元素
# out: 4 4 3
vec[c(2, 4, 3)]
# out 4 3 4

## 删除向量中的元素
vec[-2]  # 删除第二个元素
# out：1 4 3 2 2 3
vec[-2:-4] # 删除下标从2到4的所有元素
# out：1 2 2 3

## 提取满足条件的元素
vec[vec<3] # 返回vec中小于3的所有元素
# out: 1 2 2

## 找到元素
which(vec==3) # 返回等于3的下标
# out: 4 7
which.max(vec) # 返回vec的最大值的下标
# out: 2
which.min(vec) # 返回vec的最小值的下标
# out: 1
```

R
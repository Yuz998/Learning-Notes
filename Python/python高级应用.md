#### 1.求最大值、最小值、求和，均值和标准差
```python
np.mean()
np.nanmean()  ## 不包括NAN值
np.std()
np.nanstd()    ## 不包括NAN值
```
#### 2.groupby使用以及其他函数
```python
import pandas as pd
import numpy as np
ipl_data = {'Team': ['Riders', 'Riders', 'Riders', 'Kings', 'Devils', 'Devils', 'Riders',
          'Royals', 'Kings',  'Royals', 'Kings'],
         'Rank': [1, 3, 2, 4, 1, 1, 4 ,3, 2, 1, 3],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015],
         'Points':[876,789,863,673,100,200,756,788,694,701,804]}

df = pd.DataFrame(ipl_data)
print(df)

## 结果
      Team  Rank  Year  Points
0   Riders     1  2014     876
1   Riders     3  2015     789
2   Riders     2  2014     863
3    Kings     4  2015     673
4   Devils     1  2014     100
5   Devils     1  2015     200
6   Riders     4  2016     756
7   Royals     3  2017     788
8    Kings     2  2016     694
9   Royals     1  2014     701
10   Kings     3  2015     804

##  对df进行排序，按照by里面的list顺序进行排序，inplace=True，则会生成新的dataframe
df.sort_values(by=['Team','Rank'],inplace=True)

##结果
     Team  Rank  Year  Points
4   Devils     1  2014     100
5   Devils     1  2015     200
8    Kings     2  2016     694
10   Kings     3  2015     804
3    Kings     4  2015     673
0   Riders     1  2014     876
2   Riders     2  2014     863
1   Riders     3  2015     789
6   Riders     4  2016     756
9   Royals     1  2014     701
7   Royals     3  2017     788

## filter( )可以对分组进行过滤，例如筛选长度大于2的分组。reset_index(drop=True)是为了重新建立索引
df = df.groupby('Team').filter(lambda group: len(group)>2).reset_index(drop=True)

## 结果
     Team  Rank  Year  Points
0  Riders     1  2014     876
1  Riders     3  2015     789
2  Riders     2  2014     863
3   Kings     4  2015     673
4  Riders     4  2016     756
5   Kings     2  2016     694
6   Kings     3  2015     804

## apply( ）对分组进行操作，例如取每个分组中的前四个
df = df.groupby('Team').apply(lambda group: group[0:4]).reset_index(drop=True)

## 结果
     Team  Rank  Year  Points
0   Kings     4  2015     673
1   Kings     2  2016     694
2   Kings     3  2015     804
3  Riders     1  2014     876
4  Riders     3  2015     789
5  Riders     2  2014     863
6  Riders     4  2016     756
```
#### 3. 透视表pivot_table( )和交叉表crosstab( )
##### pivot_table(data，values，index，columns，aggfunc，fill_value，dropna，margins_name)
参数介绍
|
|------|--------|
|data  |	DataFrame|
|values	|待聚合的列的名称。默认聚合所有数值列
|index	|用于分组的列名或其他分组键，出现在结果透视表的行
|columns|	用于分组的列名或其他分组键，出现在结果透视表的列
|aggfunc|	聚合函数或函数列表，默认为‘mean’。可以使任何对groupby有效的函数
|fill_value	|用于替换结果表中的缺失值
|dropna|	boolean，默认为True
|margins_name|	string，默认为‘ALL’，当参数margins为True时，ALL行和列的名字


```python
df = pd.pivot_table(df,index='Rank',columns='Team',values='Points',aggfunc=[np.mean,np.std],fill_value=np.nan)

## 结果

       mean                             std
Team Devils  Kings Riders Royals     Devils
Rank                                       
1     150.0    NaN    876  701.0  70.710678
2       NaN  694.0    863    NaN        NaN
3       NaN  804.0    789  788.0        NaN
4       NaN  673.0    756    NaN        NaN
##----------------------------------------------------------------
pd.pivot_table(df, index=['Rank'], columns=['Team'], aggfunc=len, margins=True)

## 结果
     Points                           Year                        
Team Devils Kings Riders Royals All Devils Kings Riders Royals All
Rank                                                              
1       2.0   NaN    1.0    1.0   4    2.0   NaN    1.0    1.0   4
2       NaN   1.0    1.0    NaN   2    NaN   1.0    1.0    NaN   2
3       NaN   1.0    1.0    1.0   3    NaN   1.0    1.0    1.0   3
4       NaN   1.0    1.0    NaN   2    NaN   1.0    1.0    NaN   2
All     2.0   3.0    4.0    2.0  11    2.0   3.0    4.0    2.0  11

##----------------------------------------------------------------
pd.crosstab(df.Rank, data.Team, margins=True)

## 结果
Team  Devils  Kings  Riders  Royals  All
Rank                                    
1          2      0       1       1    4
2          0      1       1       0    2
3          0      1       1       1    3
4          0      1       1       0    2
All        2      3       4       2   11
```

#### 4.当csv表太大，pandas直接读取不了，则可以分块读取

 ```python
chunksize = 10000000  ## 每次读取的行数
for i, df_chunk in enumerate(pd.read_csv(filepath+'CHARTEVENTS.csv', iterator=True,chunksize=chunksize)):
    ## 查询满足条件的记录
    df = df_chunk[df_chunk['SUBJECT_ID'].isin(sub) & df_chunk['HADM_ID'].isin(hadm)]

```

#### 5.词云
```python
from wordcloud import WordCloud
import matplotlib.pyplot as plt

## text为字符串str
wordcloud = WordCloud().generate(text)
plt.figure(figsize = (8,8))
plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis("off")
plt.show()
```
![d1e7bd13dc399891ef6e61745fef4ca2.png](en-resource://database/543:0)

#### 6.matplotlib画图处理中文乱码

```python
plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文字体设置-黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
sns.set(font='SimHei')  # 解决Seaborn中文显示问题并调整字体大小
```

#### 7.Pandas&Numpy设置显示全部信息

```python
#  显示500行500列，若要显示所有行和列，则为None
pd.options.display.max_columns = 500
pd.options.display.max_rows = 500
# 显示所有行和列
np.set_printoptions(threshold=np.inf)

```
#### 8. pandas读取大文件

```python
for i, df_chunk in enumerate(pd.read_csv(path, iterator=True, chunksize=chunksize)):
    print(df_chunk)
```

#### 9. str转datatime

```
def tra_time(t):
	'''
	将str转datatime 
    '''
    if t[4:5] == '/':
        return datetime.datetime.strptime(t,'%Y/%m/%d %H:%M:%S')
    else:
        return datetime.datetime.strptime(t,'%Y-%m-%d %H:%M:%S')

def get_days(x):
	'''
	x: datetime.timedelta()类型
	'''	
    return (x.days+x.seconds/3600.)
```
### 缺失值处理

<img src="D:\Learning Notes\Deep Learning\impute.png" alt="impute" style="zoom:33%;" />

#### 一、缺失值标记生成mask数组

```python
from sklearn.impute import MissingIndicator
import numpy as np
import pandas as pd
x = np.array([[np.nan,np.nan,1.1,3],
              [4.4,np.nan,0.6,np.nan],
              [8,np.nan,1.2,0.3],
              [3,5,np.nan,2],
              [1,7,3,6],
              [5,np.nan,3,5],
              [3,8,2,1],
              [1.3,4.6,2.3,1.9]])
## 标记缺失值
indicator = MissingIndicator(missing_values=np.nan, features='all')
mask = ~indicator.fit_transform(x)
mask = mask.astype(int)
mask
OUT：
	array([[0, 0, 1, 1],
       [1, 0, 1, 0],
       [1, 0, 1, 1],
       [1, 1, 0, 1],
       [1, 1, 1, 1],
       [1, 0, 1, 1],
       [1, 1, 1, 1],
       [1, 1, 1, 1]])
```

#### 二、缺失值插补

##### 1.sklearn.Imputer  (https://scikit-learn.org/stable/modules/classes.html#module-sklearn.impute)

###### 1)  简单插补SimpleImputer

`sklearn.impute.SimpleImputer`(*, missing_values=nan, strategy='mean', fill_value=None, verbose=0, copy=True, add_indicator=False)

**Parameters：missing_values：**number，string，np.nan(default) or None

​						 **strategy:  **string, default='mean' , median, most_frequent, constant

​                          **fill_value:  **当strategy为constant时，missing_value被fill_value替换

```python
from sklearn.impute import SimpleImputer
## 均值填充（mean，）
imp_mean = SimpleImputer(missing_values=np.nan, strategy='mean')
imp_mean.fit_transform(x)
imp_mean
OUT:
    array([[3.67142857, 6.15      , 1.1       , 3.        ],
       [4.4       , 6.15      , 0.6       , 2.74285714],
       [8.        , 6.15      , 1.2       , 0.3       ],
       [3.        , 5.        , 1.88571429, 2.        ],
       [1.        , 7.        , 3.        , 6.        ],
       [5.        , 6.15      , 3.        , 5.        ],
       [3.        , 8.        , 2.        , 1.        ],
       [1.3       , 4.6       , 2.3       , 1.9       ]])
```

###### 2) 迭代插补IterativeImputer

`sklearn.impute.IterativeImputer`(*estimator=None*, *, *missing_values=nan*, *sample_posterior=False*, *max_iter=10*, *tol=0.001*, *n_nearest_features=None*, *initial_strategy='mean'*, *imputation_order='ascending'*, *skip_complete=False*, *min_value=None*, *max_value=None*, *verbose=0*, *random_state=None*, *add_indicator=False*)

**Parameters: estimator: **estimator object, default=BayesianRidge()

​						 **missing_values: ** int, np.nan, default=np.nan

​						 **sample_posterior: **boolean, default=False

​						 **max_iter: **int, default=10

​						 **n_nearest_features: **int, default=None

​						**initial_strategy: **str, default=’mean’  用于初始化缺失值的策略，可以为{“mean”, “median”, 														“most_frequent”, or “constant”}.		

​						**random_state: **int, RandomState instance or None, default=None

```python
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(random_state=0)
imp_mean.fit_transform(x)
imp_mean
OUT:
    array([[3.67701464, 6.15024302, 1.1       , 3.        ],
       [4.4       , 6.150176  , 0.6       , 2.55430953],
       [8.        , 6.15015168, 1.2       , 0.3       ],
       [3.        , 5.        , 1.84565689, 2.        ],
       [1.        , 7.        , 3.        , 6.        ],
       [5.        , 6.15130904, 3.        , 5.        ],
       [3.        , 8.        , 2.        , 1.        ],
       [1.3       , 4.6       , 2.3       , 1.9       ]])
```

###### 3) 迭代插补IterativeImputer

`sklearn.impute.KNNImputer`(***, *missing_values=nan*, *n_neighbors=5*, *weights='uniform'*, *metric='nan_euclidean'*, *copy=True*, *add_indicator=False*)

**Parameters：missing_values**：number, string, np.nan or None, default=`np.nan`

​						  **n_neighors: **int, default=5

​					 	 **weights:  **{‘uniform’, ‘distance’} or callable, default=’uniform’

​						  **metric**: {‘nan_euclidean’} or callable, default=’nan_euclidean’

​				 	     **copy**: bool, default=True

​						 **add_indicator: **bool, default=False

```python
from sklearn.impute import KNNImputer
imp_knnim = KNNImputer(n_neighbors=2)
imp_knnim.fit_transform(x)
    
```



##### 2.ycimpute.imputer

######   1) EM——期望最大化

在缺失类型为随机缺失的条件下，假设模型对于完整的样本是正确的，那么通过观测数据的边际分布可以对未知参数进行极大似然估计。

极大似然的参数估计实际中常采用的计算方法是**期望值最大化(Expectation Maximization，EM）。**

①**E步：**计算期望。利用隐藏变量现有的估计值计算最大期望。

②**M步：**期望最大化求参数。

```python
from ycimpute.imputer import EM
imp_em = EM().complete(x)
imp_em
OUT: 
    [[0.  0.  1.1 3. ]
     [4.4 0.  0.6 0. ]
     [8.  0.  1.2 0.3]
     [3.  5.  0.  2. ]
     [1.  7.  3.  6. ]
     [5.  0.  3.  5. ]
     [3.  8.  2.  1. ]
     [1.3 4.6 2.3 1.9]]
```

######   2) KNN，MICE，MIDA，GAIN，MissForest

```python
from ycimpute.imputer import KNN,MICE,MissForest,MIDA,GAIN
## KNN
imp_knn = KNN().complete(x)
## MICE
imp_mice = MICE().complete(x)
## MissForest
imp_forest = MissForest().complete(x)
## MIDA
imp_mida = MIDA().complete(x)
## GAIN
img_gain = GAIN().complete(x)

imp_knn
OUT:
    EM: 
        [[0.  0.  1.1 3. ]
         [4.4 0.  0.6 0. ]
         [8.  0.  1.2 0.3]
         [3.  5.  0.  2. ]
         [1.  7.  3.  6. ]
         [5.  0.  3.  5. ]
         [3.  8.  2.  1. ]
         [1.3 4.6 2.3 1.9]]
	KNN: 
        Imputing row 1/8 with 2 missing, elapsed time: 0.000
        [[3.35588326 5.53660549 1.1        3.        ]
         [4.4        5.57678098 0.6        2.16395097]
         [8.         6.3404006  1.2        0.3       ]
         [3.         5.         1.60189809 2.        ]
         [1.         7.         3.         6.        ]
         [5.         6.2263956  3.         5.        ]
         [3.         8.         2.         1.        ]
         [1.3        4.6        2.3        1.9       ]]
    MICE: 
        [[3.768 6.206 1.1   3.   ]
         [4.4   6.58  0.6   1.453]
         [8.    6.77  1.2   0.3  ]
         [3.    5.    1.771 2.   ]
         [1.    7.    3.    6.   ]
         [5.    6.734 3.    5.   ]
         [3.    8.    2.    1.   ]
         [1.3   4.6   2.3   1.9  ]]
    GAIN: 
       	[[3.9036272 3.9132495 1.5007374 2.9670599]
         [3.8406308 4.0916443 1.5656748 2.9697201]
         [3.7539887 3.9784312 1.5539085 2.928303 ]
         [3.8905268 3.961173  1.5338404 2.8795457]
         [1.        7.        3.        6.       ]
         [3.8108037 3.8454633 1.4947381 2.8346453]
         [3.        8.        2.        1.       ]
         [1.3       4.6       2.3       1.9      ]]

```




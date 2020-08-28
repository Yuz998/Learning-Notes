import pandas as pd
import numpy as np
import xgboost as xbg
from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import PredefinedSplit
# from sklearn.externals import joblib
import pickle
# import evaluate as E



train_x = np.load('../data/train_x.npy')
train_y = np.load('../data/train_y.npy')

val_x = np.load('../data/val_x.npy')
val_y = np.load('../data/val_y.npy')

test_x = np.load('../data/test_x.npy')
test_y = np.load('../data/test_y.npy')

train_val_features = np.concatenate((train_x, val_x), axis=0)
train_val_labels = np.concatenate((train_y, val_y), axis=0)

# 将所有index初始化为0，0表示第一轮的验证集
test_fold = np.zeros(train_val_features.shape[0]) 
# 将训练集对应的index设为 -1 ，表示永远不划分到验证集中
test_fold[:train_x.shape[0]] = -1
ps = PredefinedSplit(test_fold=test_fold)

params = {
        'max_depth': range(5, 25, 5),   # 每颗树的最大深度
        'learning_rate': [0.01, 0.1, 0.2],  ## 学习率
        'n_estimators': [500, 2000, 5000],
        'min_child_weight': [2, 5, 20],    ## 每个子节点所需要的样本数量，若设置大于1，可以起到剪枝的效果
        'max_delta_step': [0.2, 1, 2],
        'subsample': [0.6, 0.8],   ## 训练每棵树时用的样本数量
        'colsample_bytree': [0.5, 0.6, 0.8],   # 训练每棵树时用的特征数量 0-1之间   
        'reg_alpha': [0, 0.25, 1],
        'reg_lambda': [0.2, 0.6, 1],
        'scale_pos_weight': [0.2, 0.6, 1],
}
       
model = XGBClassifier()

other_params = {
        'estimator': model,
        'param_grid': params,
        'cv': ps,
        'verbose':32
    }

grsearch = GridSearchCV(**other_params)
grsearch.fit(train_val_features, train_val_labels)

bst_scores = grsearch.best_score_
print("Best score: %0.3f" % bst_scores)
print("Best paramters set: ")
best_paramters = grsearch.best_estimator_.get_params()
for param_name in sorted(params.keys()):
    print("\t%s: %r" % (param_name, best_paramters[param_name]))


# save model to file
pickle.dump(grsearch, open("xgb.pickle.dat", "wb"))

## load model from file
# loaded_model = pickle.load(open("xgb.pickle.dat", "rb"))

# y_pred = loaded_model.predict(test_x)

# cutoff = 0.5
# path = './outputs'
# E.print_metrics_binary(test_y, y_pred, cutoff, path)

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/3/9 20:29
# @Author: zhangtao
# @File  : lightgbmDemo.py

# -*- coding: utf-8 -*-
# author: hdq

import lightgbm as lgb
# import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

from sklearn.metrics import f1_score

def lgb_f1_score(y_hat, data):
    y_true = data.get_label()
    y_hat = np.round(y_hat) # scikits f1 doesn't like probabilities
    return 'f1', f1_score(y_true, y_hat), True



# 训练模型并预测
def train_predict_model(train_list_x, train_list_label, params, train_times=500):
    d_x = train_list_x
    d_y = train_list_label

    train_X, valid_X, train_Y, valid_Y = train_test_split(d_x, d_y, test_size=0.2, random_state=2)  # 将训练集分为训练集+验证集
    lgb_train = lgb.Dataset(train_X, label=train_Y)
    lgb_eval = lgb.Dataset(valid_X, label=valid_Y, reference=lgb_train)
    # select_suit_parameter(lgb_train)
    evals_result = {}
    print("Training...")
    bst = lgb.train(
        params,
        lgb_train,
        # categorical_feature=list(range(1, 82)),  # 指明哪些特征的分类特征
        valid_sets=[lgb_eval],
        num_boost_round=train_times,

        feval=lgb_f1_score, evals_result=evals_result

        # early_stopping_rounds=30
    )
    lgb.plot_metric(evals_result, metric='f1')
    return bst,lgb_train


# 保存预测模型
def save_models(bst, save_model_file):
    print("Saving Model...")
    bst.save_model(save_model_file)  # 保存模型


# 根据训练器预测结果
def predict_label(bst, predict_list_info):
    d_future_x = predict_list_info
    print("Predicting...")
    predict_result = bst.predict(d_future_x)  # 预测的结果在0-1之间，值越大代表预测企业失信可能性越大
    # print("acc:", metrics.accuracy_score(d_future_x, predict_result))
    # print("auc:", metrics.roc_auc_score(d_future_x, predict_result))
    return predict_result


# Grid搜索优参数
def select_suit_parameter(lgb_train, params):
    # ### 数据转换
    # print('数据转换')
    # ### 设置初始参数--不含交叉验证参数
    # print('设置参数')
    # params = {
    #     'boosting_type': 'gbdt',
    #     'objective': 'binary',
    #     'metric': 'auc',
    #     'nthread': 4,
    #     'learning_rate': 0.1
    # }
    #
    ## 交叉验证(调参)
    print('交叉验证')
    max_auc = float('0')
    best_params = {}

    # 准确率
    print("调参1：提高准确率")
    for num_leaves in range(5, 100, 5):
        for max_depth in range(3, 8, 1):
            params['num_leaves'] = num_leaves
            params['max_depth'] = max_depth

            cv_results = lgb.cv(
                params,
                lgb_train,
                seed=1,
                nfold=5,
                metrics=['auc'],
                early_stopping_rounds=10,
                verbose_eval=True
            )

            mean_auc = pd.Series(cv_results['auc-mean']).max()
            boost_rounds = pd.Series(cv_results['auc-mean']).idxmax()

            if mean_auc >= max_auc:
                max_auc = mean_auc
                best_params['num_leaves'] = num_leaves
                best_params['max_depth'] = max_depth
    if 'num_leaves' and 'max_depth' in best_params.keys():
        params['num_leaves'] = best_params['num_leaves']
        params['max_depth'] = best_params['max_depth']

    # 过拟合
    print("调参2：降低过拟合")
    for max_bin in range(5, 256, 10):
        for min_data_in_leaf in range(1, 102, 10):
            params['max_bin'] = max_bin
            params['min_data_in_leaf'] = min_data_in_leaf

            cv_results = lgb.cv(
                params,
                lgb_train,
                seed=1,
                nfold=5,
                metrics=['auc'],
                early_stopping_rounds=10,
                verbose_eval=True
            )

            mean_auc = pd.Series(cv_results['auc-mean']).max()
            boost_rounds = pd.Series(cv_results['auc-mean']).idxmax()

            if mean_auc >= max_auc:
                max_auc = mean_auc
                best_params['max_bin'] = max_bin
                best_params['min_data_in_leaf'] = min_data_in_leaf
    if 'max_bin' and 'min_data_in_leaf' in best_params.keys():
        params['min_data_in_leaf'] = best_params['min_data_in_leaf']
        params['max_bin'] = best_params['max_bin']

    print("调参3：降低过拟合")
    for feature_fraction in [0.6, 0.7, 0.8, 0.9, 1.0]:
        for bagging_fraction in [0.6, 0.7, 0.8, 0.9, 1.0]:
            for bagging_freq in range(0, 50, 5):
                params['feature_fraction'] = feature_fraction
                params['bagging_fraction'] = bagging_fraction
                params['bagging_freq'] = bagging_freq

                cv_results = lgb.cv(
                    params,
                    lgb_train,
                    seed=1,
                    nfold=5,
                    metrics=['auc'],
                    early_stopping_rounds=10,
                    verbose_eval=True
                )

                mean_auc = pd.Series(cv_results['auc-mean']).max()
                boost_rounds = pd.Series(cv_results['auc-mean']).idxmax()

                if mean_auc >= max_auc:
                    max_auc = mean_auc
                    best_params['feature_fraction'] = feature_fraction
                    best_params['bagging_fraction'] = bagging_fraction
                    best_params['bagging_freq'] = bagging_freq

    if 'feature_fraction' and 'bagging_fraction' and 'bagging_freq' in best_params.keys():
        params['feature_fraction'] = best_params['feature_fraction']
        params['bagging_fraction'] = best_params['bagging_fraction']
        params['bagging_freq'] = best_params['bagging_freq']

    print("调参4：降低过拟合")
    for lambda_l1 in [1e-5, 1e-3, 1e-1, 0.0, 0.1, 0.3, 0.5, 0.7, 0.9, 1.0]:
        for lambda_l2 in [1e-5, 1e-3, 1e-1, 0.0, 0.1, 0.4, 0.6, 0.7, 0.9, 1.0]:
            params['lambda_l1'] = lambda_l1
            params['lambda_l2'] = lambda_l2
            cv_results = lgb.cv(
                params,
                lgb_train,
                seed=1,
                nfold=5,
                metrics=['auc'],
                early_stopping_rounds=10,
                verbose_eval=True
            )

            mean_auc = pd.Series(cv_results['auc-mean']).max()
            boost_rounds = pd.Series(cv_results['auc-mean']).idxmax()

            if mean_auc >= max_auc:
                max_auc = mean_auc
                best_params['lambda_l1'] = lambda_l1
                best_params['lambda_l2'] = lambda_l2
    if 'lambda_l1' and 'lambda_l2' in best_params.keys():
        params['lambda_l1'] = best_params['lambda_l1']
        params['lambda_l2'] = best_params['lambda_l2']

    print("调参5：降低过拟合2")
    for min_split_gain in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
        params['min_split_gain'] = min_split_gain

        cv_results = lgb.cv(
            params,
            lgb_train,
            seed=1,
            nfold=5,
            metrics=['auc'],
            early_stopping_rounds=10,
            verbose_eval=True
        )

        mean_auc = pd.Series(cv_results['auc-mean']).max()
        boost_rounds = pd.Series(cv_results['auc-mean']).idxmax()

        if mean_auc >= max_auc:
            max_auc = mean_auc

            best_params['min_split_gain'] = min_split_gain
    if 'min_split_gain' in best_params.keys():
        params['min_split_gain'] = best_params['min_split_gain']
    print(best_params)
    return best_params

#加载模型
def load_model(model):
    # 模型加载
    bst = lgb.Booster(model_file=model)
    return bst


# 评估选取的各特征的重要度
def plot_feature_importance(dataset, model_bst):
    list_feature_name = list(dataset)
    list_feature_importance = list(model_bst.feature_importance(importance_type='split', iteration=-1))
    print(len(list_feature_name),len(list_feature_importance))
    # dataframe_feature_importance = pd.DataFrame({'feature_name': list_feature_name, 'importance': list_feature_importance})
    numlist=np.argsort(list_feature_importance)
    return {list_feature_name[one]:list_feature_importance[one] for one in numlist[::-1]}



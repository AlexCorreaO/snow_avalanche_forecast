# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 12:25:21 2023

@author: alexc
"""


from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from xgboost import XGBClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import Perceptron

from sklearn.metrics import accuracy_score, precision_recall_fscore_support
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt

# TODO: documentation

def train(X, y, mod):
    if mod == 'xg':
        model = XGBClassifier(objective="multi:softprob")
    elif mod == 'ada':
        model = AdaBoostClassifier(n_estimators=100)
    elif mod == 'svm': 
        model = SVC(kernel = 'linear', gamma = 'scale', shrinking = False,)
    elif mod == 'perceptron':
        model = Perceptron(max_iter=1000)
    elif mod == 'dt':
        model = DecisionTreeClassifier()
    elif mod == 'mlp':
        model = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(100, 100))
    else: 
        model = RandomForestClassifier(max_depth=200,
                                       n_estimators=1000,
                                       n_jobs=-1)
    model.fit(X, y)
    return model

# TODO: documentation

def predict(model, X):
    return model.predict(X)


def conf_matrix(y_test, y_pred, labels):
    labels = sorted(labels)
    cm = confusion_matrix(y_test, y_pred, labels=labels)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)
    disp.plot()
    plt.show()


def test(y_true, y_pred):
    rf_acc = accuracy_score(y_true, y_pred)
    rf_precision, rf_recall, rf_f1score, _ = \
        precision_recall_fscore_support(y_true, y_pred, average='weighted')
    print("Model Accuracy:", rf_acc)
    print("Model Precision:", rf_precision)
    print("Model Recall:", rf_recall)
    print("Model F1 Score:", rf_f1score)
    levels = y_true['dangerLevel'].unique()
    print('---------------------------------------------')
    report = classification_report(y_true, y_pred)
    print(report)
    print('---------------------------------------------')
    conf_matrix(y_true, y_pred, levels)
        

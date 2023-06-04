# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 12:05:45 2023

@author: alexc
"""


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# TODO: documentation

# This train test split is for train / validation (adjust hyperparameters)
def train_valid_split(data: pd.DataFrame, target: str = 'dangerLevel',
                      train_size=0.7):
    X = data.drop(columns=target)
    y = data[[target]]
    if train_size == 0.0:
        return np.nan, X, np.nan, y
    return train_test_split(X, y, train_size=train_size)


    
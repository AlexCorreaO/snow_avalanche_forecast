# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 19:19:01 2023

@author: alexc
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def data_analysis(df: pd.DataFrame):
    
    # print(df.describe())
    
    sh = df.shape
    
    # N Columns
    print('# Columns: '+str(sh[1]))
    
    # N rows
    print('# Rows: '+str(sh[0]))
    
    # N rows for each danger level
    s_danger = df['dangerLevel']
    counts1 = s_danger.value_counts().sort_index()
    print('Counts danger level:')
    print(counts1)
    
    # counts plot  
    # sns.set_palette('pastel')
    # sns.histplot(data=df, x='dangerLevel', stat='count')
    sns.catplot(data=df, x="dangerLevel", kind="count", palette="ch:.25",
                aspect=1.5)
    plt.show()
    
    print('Frequency danger level:')
    print(counts1/len(s_danger))
    
    # correlation between cols and danger Level
    df_corr = df.corr()[['dangerLevel']]
    danger_corr = df_corr.reindex(df_corr['dangerLevel'].abs()\
                                  .sort_values(ascending=False).index)
    pd.set_option('display.max_rows', None)
    print('dangerLevel Correlations:')
    print(danger_corr['dangerLevel'])
    
    """
    print('Correlation Matrix:')
    df_corr_mat = df.corr()
    sns.heatmap(df_corr_mat, annot=True, cmap='coolwarm')
    plt.show()
    """
    
    
    

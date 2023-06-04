# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 11:47:51 2023

@author: alexc
"""


import pandas as pd
import os


# TODO: documentation
# The set parameter separates between train and test (test not seen rows)
class get_data:
    
    def __init__(self, project_dir: str, set_t: str, features: list = []):
        self.project_dir = project_dir
        self.set = set_t
        self.rf1 = pd.DataFrame()
        self.rf2 = pd.DataFrame()
        self.cp_data = pd.DataFrame()
        self.features = features

    def get_rf1(self):
        os.chdir(self.project_dir)
        data = pd.read_csv('data/Data_RF1_forecast.csv', index_col=0)
        if self.set:
            data = data[data['set'] == self.set]
        if len(self.features) > 1:
            data = data[self.features]
        self.rf1 = data.reset_index(drop=True)
    
    def get_rf2(self):
        os.chdir(self.project_dir)
        data = pd.read_csv('data/Data_RF2_tidy.csv', index_col=0)
        if self.set:
            data = data[data['set'] == self.set]
        if len(self.features) > 1:
            data = data[self.features]
        self.rf2 = data.reset_index(drop=True)
        
    def get_copernicus_data(self):
        pass
        
    def data_filtering(self):
        self.rf1 = self.rf1.dropna()
        self.rf2 = self.rf2.dropna()
        
    def study_data(self):
        counts1 = self.rf1['dangerLevel'].value_counts().sort_index()
        print('Counts danger level RF1:')
        print(counts1)
        # counts2 = self.rf2['dangerLevel'].value_counts().sort_index()
        # print('Counts danger level RF2:')
        # print(counts2)
        
if __name__ == '__main__':
    
    project_path = r'C:\Users\alexc\OneDrive\Escritorio\UNI\4t\TFG\rep_article'
    train_data = get_data(project_dir=project_path, set_t='train')
    train_data.get_rf1()
    train_data.get_rf2()
    
    test_data = get_data(project_dir=project_path, set_t='test')
    test_data.get_rf1()
    test_data.get_rf2()
    

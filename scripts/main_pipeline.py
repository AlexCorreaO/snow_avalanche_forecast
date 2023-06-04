# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 12:26:24 2023

@author: alexc
"""


from upload_data import get_data
from utils import train_valid_split
from train import train, test, predict
from data_analysis import data_analysis
import numpy as np
import pandas as pd
import shap
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # Main directory: # TODO: set directory path
    project_path = r'C: '
    
    # get full data (when features is empty, gives all columns) for data 
    #   analysis
    print('\nGET FULL DATA')
    analysis_data = get_data(project_dir=project_path, set_t=None,
                          features=[])
    analysis_data.get_rf1()
    rf1 = analysis_data.rf1
    
    # data analysis
    print('\nDATA ANALYSIS')
    data_analysis(analysis_data.rf1)
    an = analysis_data.rf1
    desc = analysis_data.rf1.describe()
    desc1 = an[an['dangerLevel']==1].describe()
    desc2 = an[an['dangerLevel']==2].describe()
    desc3 = an[an['dangerLevel']==3].describe()
    desc4 = an[an['dangerLevel']==4].describe()
    desc5 = an[an['dangerLevel']==5].describe()
    
    # Feature selection
    input_features = ['HN24', 'HN24_7d', 'HN72_24', 'HS_mod', 'ILWR', 
                      'ISWR_diff', 'ISWR', 'LWR_net', 'MS_Snow', 'Qg0',
                      'Qs', 'Qw', 'RH', 'S4', 'Sn', 'Ss', 'TA', 'TSS_mod',
                      'VW_drift', 'VW', 'ccl_pwl_100', 'min_ccl_pen',
                      'pAlbedo', 'Pen_depth','sn38_pwl_100', 'wind_trans24',
                      'wind_trans24_3d', 'wind_trans24_7d', 'zSn', 'zSs',
                      'dangerLevel']
    
    # Train Data
    print('\nTRAIN DATA')
    train_data = get_data(project_dir=project_path, set_t='train',
                          features=input_features)
    train_data.get_rf1()
    train_data.get_rf2()
    train_data.data_filtering()
    
    # Test Data
    print('\nTEST DATA')
    test_data = get_data(project_dir=project_path, set_t='test',
                         features=input_features)
    test_data.get_rf1()
    test_data.get_rf2()
    test_data.data_filtering()
    
    # Train / Validation Data
    print('\nTRAIN / VALID. SPLIT')
    X_train, X_val, y_train, y_val = train_valid_split(train_data.rf1, 
                                                       target='dangerLevel')
    
    X_, X_test, y_, y_test = train_valid_split(test_data.rf1, 
                                                       target='dangerLevel',
                                                       train_size=0.0)
    mod = 'rf'
    # rf, xg, ada, svm, perceptron, dt, mlp
    if mod == 'xg':
        y_train -= 1.0
        y_val -= 1.0
        y_test -= 1.0
    # Train and predict over validation data
    print('\nTRAIN AND PREDICTION on Validation')
    model = train(X_train, np.ravel(y_train).astype(int), mod)
    y_pred = predict(model, X_val)
    
    # Precision, recall and scores
    print('\nPRECISION AND SCORES on Validation')
    test(y_val, y_pred)
    
    print('\nPRECISION OF EACH REGION')
    results_df = pd.DataFrame({'y_val': y_val['dangerLevel'].values,
                               'y_pred': y_pred.flatten()}, index=y_val.index)
    results_df_sector = results_df.merge(rf1[['sector_id']], left_index=True,
                                         right_index=True)
    results_df_sector['sector_id'] = results_df_sector['sector_id'].\
        astype(str).str[0]
    accuracy_by_region = results_df_sector.groupby('sector_id').\
        apply(lambda x: (x['y_val'] == x['y_pred']).mean())
    print(accuracy_by_region)
    
    # Train and predict over test data
    print('\nPREDICTION on Test')
    y_pred_test = predict(model, X_test)
    
    # Precision, recall and scores
    print('\nPRECISION AND SCORES on Test')
    test(y_test, y_pred_test)
    
    # Feature Importance
    print('\nFEATURE IMPORTANCE')
    importance = pd.Series(model.feature_importances_, index=X_train.columns)\
        .sort_values(ascending=False)
    print(importance)
    
    """
    print('Feature importance with SHAP:')

    explainer = shap.KernelExplainer(model.predict_proba, X_train.sample(n=100))
    # Generate SHAP values using the pipeline
    X_val_red = X_val.sample(n=100)
    shap_values = explainer.shap_values(X_val_red)
    
    # Plot the SHAP summary plot
    shap.summary_plot(shap_values, X_val, class_names=model.classes_,
                      max_display=X_val.shape[1])
    
    # Calculate the mean SHAP values
    mean_shap_values = np.mean(shap_values, axis=0)
    
    shap.summary_plot(mean_shap_values, X_val_red, class_names=model.classes_, 
                      max_display=X_val_red.shape[1])
    """
    """
    y_pred_red = model.predict(X_val_red)
    # Loop over each dangerLevel class
    for class_label in np.unique(y_train):
        print(class_label)
        # Select data points belonging to the specific class
        X_class = X_val_red[y_pred_red == class_label]
    
        # Generate SHAP values for the class
        explainer = shap.KernelExplainer(model.predict_proba, X_train.sample(n=100))
        shap_values = explainer.shap_values(X_class)
    
        # Loop over the instances of the specific class
        for i in range(len(X_class)):
            # Create the waterfall plot for the instance
            shap.plots.waterfall(shap_values[i], show=False)
            
            # Customize the plot title
            plt.title(f"Waterfall Plot - Class {class_label}")
    
            # Display the plot
            plt.show()

    """
    # End
    print('MAIN PIPELINE FINISHED')


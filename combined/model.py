#tabular data imports :
import pandas as pd
import numpy as np
from pydataset import data

# visualization imports:
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

# success metrics from earlier in the week: mean squared error and r^2 explained variance
from sklearn.preprocessing import MinMaxScaler, PolynomialFeatures
from sklearn.cluster import KMeans
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

#stats
from scipy.stats import pearsonr, spearmanr
from scipy.stats import shapiro

import warnings
warnings.filterwarnings("ignore")
import wrangle as w
import os
directory = os.getcwd()
pd.set_option('display.max_columns', None)


def split_data(df, test_size=0.2, random_state=123):
    train, test = train_test_split(df, test_size=test_size, random_state=random_state)
    train, validate = train_test_split(train, test_size=test_size, random_state=random_state)
    return train, validate, test

def processed_wine(df):
    # Encode categorical variables
    # Assuming 'color' is the only categorical column that needs encoding
    color_dummies = pd.get_dummies(df['color'], drop_first=True)
    df = pd.concat([df, color_dummies], axis=1)
    df = df.drop(columns=['color','wine_quality'])

    # Split data
    train, validate, test = split_data(df)

    # Identify continuous features for scaling
    # Assuming all columns except 'quality_category' are continuous
    continuous_cols = train.columns.difference(['quality_category'])

    # Scale continuous features
    scaler = MinMaxScaler()
    train[continuous_cols] = scaler.fit_transform(train[continuous_cols])
    validate[continuous_cols] = scaler.transform(validate[continuous_cols])
    test[continuous_cols] = scaler.transform(test[continuous_cols])

    return train, validate, test

def evaluate_reg(y, yhat):
    '''
    based on two series, y_act, y_pred, (y, yhat), we
    evaluate and return the root mean squared error
    as well as the explained variance for the data.
    
    returns: rmse (float), rmse (float)
    '''
    rmse = mean_squared_error(y, yhat, squared=False)
    r2 = r2_score(y, yhat)
    return rmse, r2

def model_prep_wine_scaled(X_train, X_validate, X_test):
    '''Takes the X train, validate, and test and fits them to a RobustScaler
    
    
    return X_train_scaled, X_validate_scaled, X_test_scaled'''
    # makes a copy of the dataframes
    X_train_scaled = X_train.copy()
    X_valid_scaled = X_validate.copy()
    X_test_scaled = X_test.copy()

    columns_to_scale = ['fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar',
       'chlorides', 'free_sulfur_dioxide', 'total_sulfur_dioxide', 'density',
       'pH', 'sulphates', 'alcohol']

    scaler = RobustScaler()

    X_train_scaled[columns_to_scale] = scaler.fit_transform(X_train[columns_to_scale])
    X_valid_scaled[columns_to_scale] = scaler.transform(X_validate[columns_to_scale])
    X_test_scaled[columns_to_scale] = scaler.transform(X_test[columns_to_scale])

    return X_train_scaled, X_valid_scaled, X_test_scaled
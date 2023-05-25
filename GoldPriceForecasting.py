import streamlit as st
import flet as ft

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")

# create data drame to read data set
df = pd.read_csv('gld_price_data.csv')
df.head()

# check the df structure
df.info()

# find number of rows and columns
df.shape

# describe df numerical columns
df.describe()

# find unique values from categorical features
for col in df.select_dtypes(include = 'object').columns:
    print(col)
    print(df[col].unique())
    
# find missing values
features_na = [features for features in df.columns if df[features].isnull().sum() > 0]
for feature in features_na:
    print(feature, np.round(df[feature].isNull().mean(), 4), ' % missing values')
else:
    print("No missing value found")

for column in df.columns:
    print(column, df[column].nunique())

# explore the Categorical Features
categorical_features = [feature for feature in df.columns if((df[feature].dtypes == 'O') & (feature not in ['GLD']))]
categorical_features

for feature in categorical_features:
    print('The Feature is {} and number of categories are {}'.format(feature, len(df[feature].unique())))
    
# explore the Numerical Features #
# List of numerical variables
numerical_features = [feature for feature in df.columns if((df[feature].dtypes != 'O') & (feature not in ['GLD']))]
print('Number of numerical variables: ', len(numerical_features))

# visualize the numerical variables
df[numerical_features].head()

# Find discrete Numerical Features #
discrerte_feature = [feature for feature in numerical_features if len(df[feature].unique()) < 25]
print("Discrete Variables count: {}".format(len(discrerte_feature)))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:19:10 2020

@author: maureenkeenan
"""
#%% Import packages and load df
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

maindir = '/Users/maureenkeenan/Desktop/Kaggle/WiDs_Datathon_2020'
filepath = os.path.join(maindir,'data/external')

df = pd.read_csv(os.path.join(filepath,'training_v2.csv'))

#%% Check out the dataframe

# Look at object types and size
df.info()

# Look at our target variable: hospital_death
df.groupby('hospital_death').hospital_death.count()
# Change this to text to use with Seaborn
lgd = dict({0:'Survived',1:'Died'})
df['Survived'] = df['hospital_death'].map(lgd)

# Split this df into types
df_object = df.select_dtypes('object')
df_int = df.select_dtypes('int64')
df_float= df.select_dtypes('float64')

# %%% Review categorical 

# Handy to look at description of objects
obj_dsc = df_object.describe(include=['object']).T
obj_dsc['freqPercent'] = obj_dsc.freq/len(df_object)
obj_dsc['missingvals'] = len(df_object) - obj_dsc['count']
obj_dsc['missingvalsPercent'] = df_object.isnull().sum()/len(df_object)

print(obj_dsc)

# Are there any NaN in these columns
print(df_object.isnull().sum())

# %%% Review numeric

# Get summary stats
review = df_float.describe().T

# %%% Review NaN
# Review columns with na
cols_w_na = df.columns[df.isna().any()].to_list()

# Look at percent null
nas=pd.DataFrame(df.isnull().sum().sort_values(ascending=False)/len(df),columns = ['percent'])
pos = nas['percent'] > 0
print(nas[pos])

#%% Drop data

# Drop columns where 50% of the column is NaN
df_out = df.dropna(axis =1, thresh = len(df)*.50 )


#%% Fillna

#%%% Categorical

# Get list of columns to work through
cols_w_na = df_object.columns[df_object.isna().any()].to_list()
print(cols_w_na)

#%%%% Ethnicty
df_object['ethnicity'].value_counts().plot(kind='bar')
plt.title('Ethnicity Histogram')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

df_out['ethnicity'].fillna('Other/Unknown',inplace=True)
df_out['ethnicity'].isnull().sum()

#%%%% Gender

# Only 25 missing rows
# Drop rows where gender is missing as its 0 .02% of the data
df_out = df_out['gender'].dropna(axis=0)

#%%%% Hospital_admit_source

# 25% of the data is missing a hospital_admit_source
plt.figure(2)
df_object['hospital_admit_source'].value_counts().plot(kind='bar')
plt.title('hospital_admit_source Histogram')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Drop this score in favor of keeping icu_admit_source
df_out.drop(columns = 'hospital_admit_source', inplace=True)

#%%%% icu_admit_source
plt.figure(1)
df_object['icu_admit_source'].value_counts().plot(kind='bar')
plt.title('icu_admit_source Histogram')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# 1.2% of the data is missing. Most admits are from Accident & Emergency. Fill with those
df_out['icu_admit_source'].fillna('Accident & Emergency',inplace=True)
df_out['icu_admit_source'].nunique
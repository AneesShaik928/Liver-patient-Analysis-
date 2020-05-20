# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 04:47:53 2019

@author: Rammohan
"""

#import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Read the dataset/Data Preprocessing
data=pd.read_csv('concrete_data.csv')
data

data.head()

#checking null values in the dataset
data.isnull().any()

x=data.iloc[:,:8]
x=data.iloc[:,:8].values
x

x.ndim

y=data.iloc[:,-1:]
y
y= data.iloc[:,-1:].values
y
#split the data intlo train and test
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

x_test
#plot the variance between parameters
plt.hist((data.concrete_compressive_strength))

data.hist()
#correlation between the variables
data.corr()
sns.heatmap(data)
#model
from sklearn.linear_model import LinearRegression
mr=LinearRegression()
mr.fit(x_train,y_train)

y_predict =mr.predict(x_test)
y_predict


import pickle
pickle.dump(mr,open('strength.pkl','wb'))
model=pickle.load(open('strength.pkl','rb'))












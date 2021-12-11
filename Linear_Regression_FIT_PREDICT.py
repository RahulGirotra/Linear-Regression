#!/usr/bin/env python
# coding: utf-8

# In[1]:


class My_Linear_Regression:
    def __init__(self):
        self.m =None
        self.b =None
    def fit(self,X_train,y_train):
        num=0
        den=0
        for i in range(X_train.shape[0]):
            num=num + (X_train[i] - X_train.mean())*(Y_train[i] - Y_train.mean())
            den=den + (X_train[i] - X_train.mean())*(X_train[i] - X_train.mean())
        self.m = num/den
        self.b = y_train.mean()-(self.m*X_train.mean())
    def predict(self,X_test):
        return self.m*X_test +self.b


# In[ ]:





from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd

class ROHImputer(BaseEstimator, TransformerMixin):
    def __init__(self): # no *args or **kargs
        print('Yo we are in')
    
    def fit(self, X, y=None):
        return self # nothing else to do 
    
    def transform(self, df=None):
        if not df.empty:
            targetdates = df['TargetDate'].unique()
            # Bad solution
            for targetdate in targetdates:
                df[df['TargetDate']==targetdate] = df[df['TargetDate']==targetdate].ffill().bfill()
        return df
    

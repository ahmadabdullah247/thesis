from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd

class TypePreprocess(BaseEstimator, TransformerMixin):
    def __init__(self): # no *args or **kargs
        print('Yo we are in')
    
    def fit(self, X, y=None):
        return self # nothing else to do 
    
    def transform(self, df=None):
        if not df.empty:
            # Object to datetime 
            df['TargetDate'] = pd.to_datetime(df['TargetDate'],format="%Y-%m-%d")
            df['SnapshotDate'] = pd.to_datetime(df['SnapshotDateTime'].dt.date,format="%Y-%m-%d")
            # Create new Column
            df['LeadTime'] = (df['TargetDate']-df['SnapshotDate']).astype('timedelta64[D]')
            # Droping SnapshotDateTime because we don't need time component
            df = df.drop(columns=['SnapshotDateTime'])
            df = df.drop_duplicates(subset=['HotelId','TargetDate','SnapshotDate'],keep='last')

            # Drop rows with snapshot date grater then targetdate 
            df = df[df['SnapshotDate']<=df['TargetDate']]
            # Only consider 90 days development
            df = df[df['LeadTime']<90]
            # sorting
            df = df.sort_values(by=['TargetDate','SnapshotDate'], ascending=True)

        return df
    

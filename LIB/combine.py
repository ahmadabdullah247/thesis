import pandas as pd


def combine(hotelId):
    # retriving data from files
    df_occ = pd.read_pickle('/Users/ahmadabdullahtariq/Documents/Projects/thesis/dataset/preprocessed/occupancy.pkl')
    df_pri = pd.read_pickle('/Users/ahmadabdullahtariq/Documents/Projects/thesis/dataset/preprocessed/price.pkl')

    # filter data for hotel 284
    df_occ = df_occ[df_occ.HotelId==hotelId]
    df_pri = df_pri[df_pri.HotelId==hotelId]

    # dropping columns that we are not going to use
    df_occ = df_occ.drop(columns=['LeadTime', 'HotelId'])
    df_pri = df_pri.drop(columns=['LeadTime', 'HotelId'])

    # drop duplicates 
    df_occ = df_occ.drop_duplicates(subset=['TargetDate', 'SnapshotDate'], keep='last')
    df_pri = df_pri.drop_duplicates(subset=['TargetDate', 'SnapshotDate'], keep='last')

    # Definitive and Rooms have NaN so we can't convert them astype int.
    # Work around this is to convert it into float, this would make it easier to fill in next steps
    df_occ['Definitive'] = df_occ['Definitive'].astype('float')
    df_occ['Rooms']      = df_occ['Rooms'].astype('float')
    
    # We can see that length of both dataframe is different
    # So we are going to use outter joing to include all possible dates and their development
    df = pd.merge(df_occ, df_pri, left_on=['TargetDate','SnapshotDate'], right_on=['TargetDate','SnapshotDate'], how='outer')

    #Some preprocessing steps
    ## Sort according to TargetDate and Snapshot dataset
    ## Drop duplicate entries
    ## Reset index
    df = df.sort_values(by=['TargetDate','SnapshotDate'])
    df = df.drop_duplicates(subset=['TargetDate', 'SnapshotDate'], keep='last')
    df = df.reset_index(drop=True)

    # Forward and Backword fill within each target date.
    targetdates = df['TargetDate'].unique()
    # Bad solution
    for targetdate in targetdates:
        df[df['TargetDate']==targetdate] = df[df['TargetDate']==targetdate].ffill().bfill()
        df[df['TargetDate']==targetdate] = df[df['TargetDate']==targetdate].ffill().bfill()
        df[df['TargetDate']==targetdate] = df[df['TargetDate']==targetdate].ffill().bfill()
    
    df = df[~df['LAR'].isna()]
    
    # replace zero entries of rooms with forwardfill
    df['Rooms'] = df['Rooms'].replace(to_replace=0, method='ffill')
    # normalize overbooking
    df.loc[(df['Definitive']>df['Rooms']),'Definitive'] = df[df['Definitive']>df['Rooms']]['Rooms']

    # consider data for 2018 and 2019
    df = df[df['TargetDate']<='2019-12-31']
    # creating new columns
    df['SnapshotDate'] = (df['TargetDate']-df['SnapshotDate']).dt.days
    df['DOW'] = df.TargetDate.dt.dayofweek
    # df = df.drop(columns=['SnapshotDate'])
    # just rearrange columns 
    df = df.rename(columns={'TargetDate': 'DOA','SnapshotDate':'LeadTime','DOW':'DOW','LAR':'Price','Rooms':'TotalCapacity','Definitive':'ROH'}) 
    df = df[['DOA','LeadTime','DOW','Price','TotalCapacity','ROH']]
    df.to_pickle("/Users/ahmadabdullahtariq/Documents/Projects/thesis/dataset/preprocessed/"+str(hotelId)+"_imputed.pkl")
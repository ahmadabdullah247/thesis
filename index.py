import streamlit as st
import pandas as pd 
from datetime import datetime
import plotly.graph_objects as go

@st.cache
def load_data():
    try:
        df =  pd.read_pickle('dataset/preprocessed/combined.pkl')
        df_imputed =  pd.read_pickle('dataset/preprocessed/imputed.pkl')
        return df,df_imputed
    except:
        print('Something went wrong')
        return None

def plot(df):
    fig1 = go.Figure(data=go.Heatmap(x=df['TargetDate'], y=df['SnapshotDate'], z=df['Definitive'], colorscale='Viridis'))
    fig1.update_layout(
                    title='Definative Values of Hotel',
                    xaxis=dict(
                        #     rangeselector=dict(
                        #         buttons=list([
                        #                 dict(count=1,label="1m",step="month",stepmode="backward"),
                        #                 dict(count=6,label="6m",step="month",stepmode="backward"),
                        #                 dict(count=1,label="YTD",step="year",stepmode="todate"),
                        #                 dict(count=1,label="1y",step="year",stepmode="backward"),
                        #                 dict(step="all")])
                        #     ),

                            rangeslider=dict(visible=True),
                            type="date", 
                            title_text = "Target date"
                    ), 
                    yaxis = dict(title_text = 'Lead Time (days)',autorange="reversed")
     )

    fig2 = go.Figure(data=go.Heatmap(x=df['TargetDate'], y=df['SnapshotDate'], z=df['Rooms'], colorscale='Viridis'))
    fig2.update_layout(
                    title='Definative Values of Hotel',
                    xaxis=dict(
                        #     rangeselector=dict(
                        #         buttons=list([
                        #                 dict(count=1,label="1m",step="month",stepmode="backward"),
                        #                 dict(count=6,label="6m",step="month",stepmode="backward"),
                        #                 dict(count=1,label="YTD",step="year",stepmode="todate"),
                        #                 dict(count=1,label="1y",step="year",stepmode="backward"),
                        #                 dict(step="all")])
                        #     ),

                            rangeslider=dict(visible=True),
                            type="date", 
                            title_text = "Target date"
                    ), 
                    yaxis = dict(title_text = 'Lead Time (days)',autorange="reversed")
     )

    fig3 = go.Figure(data=go.Heatmap(x=df['TargetDate'], y=df['SnapshotDate'], z=df['LAR'], colorscale='Viridis'))
    fig3.update_layout(
                    title='Definative Values of Hotel',
                    xaxis=dict(
                        #     rangeselector=dict(
                        #         buttons=list([
                        #                 dict(count=1,label="1m",step="month",stepmode="backward"),
                        #                 dict(count=6,label="6m",step="month",stepmode="backward"),
                        #                 dict(count=1,label="YTD",step="year",stepmode="todate"),
                        #                 dict(count=1,label="1y",step="year",stepmode="backward"),
                        #                 dict(step="all")])
                        #     ),

                            rangeslider=dict(visible=True),
                            type="date", 
                            title_text = "Target date"
                    ), 
                    yaxis = dict(title_text = 'Lead Time (days)',autorange="reversed")
     )     
    return fig1,fig2,fig3


def main():
    df,df_imputed = load_data()
    hotelIds = df.HotelId.unique()

    st.subheader('City Analysis')
    hotelId = st.sidebar.selectbox('Select hotel',hotelIds)
    # start_date = st.sidebar.date_input('Start date', datetime(2018, 1, 1))
    # end_date   = st.sidebar.date_input('End date', datetime(2018, 6, 1))
    # print(df['TargetDate']>=start_date)
    isImputed = st.sidebar.checkbox('Impute Values')
    if hotelId:
        if isImputed:
            filtered = df_imputed[(df_imputed['HotelId']==hotelId)]# & (df['TargetDate']>=start_date) & (df['TargetDate']<=end_date)]
        else:
            filtered = df[(df['HotelId']==hotelId)]# & (df['TargetDate']>=start_date) & (df['TargetDate']<=end_date)]
        definative,rooms,prices = plot(filtered)
        st.write(definative)
        st.write(rooms)
        st.write(prices)

        st.subheader('Hotel Description')
        st.write(df.describe())

if __name__ == "__main__":
    main()


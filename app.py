import streamlit as st
import pandas as pd
import numpy as np
import sqlite3
import datetime
from AssetAllocation.ChangeLevAsset import ChangeKorAsset

#from DB.db_helper import execute_sql
global Strategy,time_range_inp
  
def ReadData(db_name, sql, param={}):
    with sqlite3.connect('{}.db'.format(db_name)) as con:
        cur = con.cursor()
        cur.execute(sql, param)
        cols = [column[0] for column in cur.description]
        results= pd.DataFrame.from_records(data = cur.fetchall(), columns = cols)
    
        return results

def form_callback():
    
    Strategy_inp = Strategy
    #time_range_inp = time_range

with st.sidebar.form(key='my_form'):
    
    st.subheader('Created by GOMBAL')
    
    #Strategy = st.sidebar.selectbox("Choose Asset Strategy",("VAA", "DAA", "BAA"))
    #Min_Time = st.sidebar.date_input("Select Start Date", datetime(2022,11,1))
    
    #st.sidebar.write("Min time is : ",Min_Time)
    
    #Submitted = st.form_submit_button(label='Calculate!')
    
    #if Submitted:
    #    st.write("When you run the model, compositions will be rescaled to ensure they sum to 100%.")
    
st.header("Asset Allocation")

sql = "select * from AA_T"
df_DB_Temp = ReadData('AA_Today', sql)
df_DB_T = df_DB_Temp.set_index(keys=['index'], inplace=False, drop=False)
df_DB_T = df_DB_T.drop(['index'], axis = 1, inplace=False)

st.caption("Asset Momentums")

st.caption("Today's Asset Choice : Global")
st.dataframe(df_DB_T[['DAA','VAA','BAA','ABAA','ODM']].iloc[[1,2]],use_container_width=True)

st.caption("Today's Asset Choice : Korea")
df_DB_K = df_DB_T[['DAA','VAA','BAA','ABAA','ODM']].iloc[[1,2]]
df_DB_TK = ChangeKorAsset(df_DB_K)
print(df_DB_TK)
st.dataframe(df_DB_TK,use_container_width=True)

#st.dataframe(df_DB_TK,use_container_width=True)

sql = "select * from AA"
df_DB = ReadData('AA_Data', sql)
DB_col_list = list(df_DB)

df_DB['Date'] = pd.to_datetime(df_DB['index'], infer_datetime_format=True)
df_DB['Date'] = df_DB["Date"].dt.strftime("%Y-%m-%d")
df_DB['Date'] = pd.to_datetime(df_DB['Date'], infer_datetime_format=True)  
df_DB = df_DB.set_index(keys=['Date'], inplace=False, drop=True)

st.caption("BackTest Result")
st.dataframe(df_DB_T[['DAA','VAA','BAA','ABAA','ODM']].iloc[[3,4]],use_container_width=True)

st.caption("BackTest Result : CAGR")
st.line_chart(data=df_DB[['VAA_BAL','DAA_BAL','BAA_BAL','ABAA_BAL','ADM_BAL']], use_container_width=True)
st.caption("BackTest Result : MDD")
st.area_chart(data=df_DB[['VAA_DD','DAA_DD','BAA_DD','ABAA_DD','ADM_DD']], use_container_width=True)

#st.dataframe(df_DB)

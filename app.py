import streamlit as st
import pandas as pd
import numpy as np
import sqlite3
import datetime
from AssetAllocation.ChangeLevAsset import ChangeKorAsset
from Momentum.Momentum_Chart import Mom_Chart

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
    
    Submitted = st.form_submit_button(label='Calculate!')
    
    if Submitted:
        st.write("When you run the model, compositions will be rescaled to ensure they sum to 100%.")
    
st.header("Asset Allocation")

Lev_Strategy = st.radio("Select Leverage Strategy", ('Basic', 'Leverage X2', 'Leverage X3'))
    
sql = "select * from AA_T"
df_DB_Temp = ReadData('AA_Today', sql)
df_DB_T = df_DB_Temp.set_index(keys=['index'], inplace=False, drop=False)
df_DB_T = df_DB_T.drop(['index'], axis = 1, inplace=False)

st.write("Asset Momentums")

sql = "select * from MOM"
df_DB_M_Temp = ReadData('MOM_Data', sql)
df_DB_M = Mom_Chart(df_DB_M_Temp)

st.dataframe(df_DB_M,use_container_width=True)
#st.line_chart(data=df_DB_M_Temp[Col_M], use_container_width=True)

st.write("Today's Asset Choice : Global")

if Lev_Strategy == 'Basic':
    st.dataframe(df_DB_T[['DAA','VAA','BAA','ABAA','ODM','ADM']].iloc[[1,2]],use_container_width=True)
elif Lev_Strategy == 'Leverage X2':
    st.dataframe(df_DB_T[['DAA_LV','VAA_LV','BAA_LV','ABAA_LV','ODM_LV','ADM_LV']].iloc[[1,2]],use_container_width=True)
else:pass
    
st.write("Today's Asset Choice : Korea (연금계좌)")
if Lev_Strategy == 'Basic':
    df_DB_K = df_DB_T[['DAA','VAA','BAA','ABAA','ODM','ADM']].iloc[[1,2]]
    df_DB_TK = ChangeKorAsset(df_DB_K)
    st.dataframe(df_DB_TK,use_container_width=True)
else:
    st.caption('Not Supported ..')

if Lev_Strategy == 'Basic':
    sql = "select * from AA"
    df_DB = ReadData('AA_Data', sql)
    DB_col_list = list(df_DB)
    
elif Lev_Strategy == 'Leverage X2':
    sql = "select * from AA_Lev"
    df_DB = ReadData('AA_Lev_Data', sql)
    DB_col_list = list(df_DB)
            
else:pass

df_DB['Date'] = pd.to_datetime(df_DB['index'], infer_datetime_format=True)
df_DB['Date'] = df_DB["Date"].dt.strftime("%Y-%m-%d")
df_DB['Date'] = pd.to_datetime(df_DB['Date'], infer_datetime_format=True)  
df_DB = df_DB.set_index(keys=['Date'], inplace=False, drop=True)

st.write("BackTest Result")

if Lev_Strategy == 'Basic':
    st.dataframe(df_DB_T[['DAA','VAA','BAA','ABAA','ODM','ADM']].iloc[[3,4]],use_container_width=True)
elif Lev_Strategy == 'Leverage X2':
    st.dataframe(df_DB_T[['DAA_LV','VAA_LV','BAA_LV','ABAA_LV','ODM_LV','ADM_LV']].iloc[[3,4]],use_container_width=True)
else:pass
    
st.write("BackTest Result : CAGR")
st.line_chart(data=df_DB[['VAA_BAL','DAA_BAL','BAA_BAL','ABAA_BAL','ADM_BAL','ODM_BAL']], use_container_width=True)
st.write("BackTest Result : MDD")
st.area_chart(data=df_DB[['VAA_DD','DAA_DD','BAA_DD','ABAA_DD','ADM_DD','ODM_DD']], use_container_width=True)

#st.dataframe(df_DB)

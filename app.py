import streamlit as st
#import pandas as pd
#import numpy as np
#import sqlite3

#from DB.db_helper import execute_sql

st.header("Asset Allocation")

#def form():
#    with st.form(key="information form"):
#        name = st.text_input("Enter your name : ")
#        age =  st.text_input("Enter your age : ")
#        
#        submission = st.form_submit_button(label="Submit")
#        if submission == True:
#            st.success("Successfully submit")
#
#   
#def ReadData(db_name, sql, param={}):
#    with sqlite3.connect('{}.db'.format(db_name)) as con:
#        cur = con.cursor()
#        cur.execute(sql, param)
#        cols = [column[0] for column in cur.description]
#        results= pd.DataFrame.from_records(data = cur.fetchall(), columns = cols)
#    
#        return results
#
#st.header("Asset Allocation")
#
#form()
#
#sql = "select * from AA_T"
#df_DB_T = ReadData('AA_Today', sql)
#st.subheader("Today's Asset Choice")
#st.dataframe(df_DB_T[['DAA','VAA','BAA','ABAA','ODM']],width=1000,height=150)
#
#sql = "select * from AA"
#df_DB = ReadData('AA_Data', sql)
#DB_col_list = list(df_DB)
#
#df_DB['Date'] = pd.to_datetime(df_DB['index'], infer_datetime_format=True)
#df_DB['Date'] = df_DB["Date"].dt.strftime("%Y-%m-%d")
#df_DB['Date'] = pd.to_datetime(df_DB['Date'], infer_datetime_format=True)  
#df_DB = df_DB.set_index(keys=['Date'], inplace=False, drop=True)
#        
#st.subheader("BackTest Result")
#st.line_chart(data=df_DB[['VAA_BAL','DAA_BAL','BAA_BAL','ABAA_BAL','ADM_BAL','ODM_BAL']], use_container_width=True)
#
##st.dataframe(df_DB)
#
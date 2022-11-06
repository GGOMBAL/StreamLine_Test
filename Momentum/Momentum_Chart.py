import pandas as pd
import numpy as np
import sqlite3
import datetime

def Mom_Chart(df_DB_M):

# Makeup Universe
    Universe = ['SPY','EFA','EEM','AGG','SHY','IEF','TLT','DBC','GSG','IAU']
    col = ['1Month','3Month','6Month','12Month','Total Momentum']
    indexs = ['SPY','EFA','EEM','AGG','SHY','IEF','TLT','DBC','GSG','IAU']
    
    Col_1M = ['SPY_1M','EFA_1M','EEM_1M','AGG_1M','SHY_1M','IEF_1M','TLT_1M','DBC_1M','GSG_1M','IAU_1M']
    Col_3M = ['SPY_3M','EFA_3M','EEM_3M','AGG_3M','SHY_3M','IEF_3M','TLT_3M','DBC_3M','GSG_3M','IAU_3M']
    Col_6M = ['SPY_6M','EFA_6M','EEM_6M','AGG_6M','SHY_6M','IEF_6M','TLT_6M','DBC_6M','GSG_6M','IAU_6M']
    Col_12M = ['SPY_12M','EFA_12M','EEM_12M','AGG_12M','SHY_12M','IEF_12M','TLT_12M','DBC_12M','GSG_12M','IAU_12M']
    Col_M = ['SPY_M','EFA_M','EEM_M','AGG_M','SHY_M','IEF_M','TLT_M','DBC_M','GSG_M','IAU_M']
    
    df_DB_1M = df_DB_M[Col_1M].tail(1)
    df_DB_1M.columns = [indexs]
    df_DB_1M = df_DB_1M.T
    df_DB_1M.columns = ['1Month']

    df_DB_3M = df_DB_M[Col_3M].tail(1)
    df_DB_3M.columns = [indexs]
    df_DB_3M = df_DB_3M.T
    df_DB_3M.columns = ['3Month']

    df_DB_6M = df_DB_M[Col_6M].tail(1)
    df_DB_6M.columns = [indexs]
    df_DB_6M = df_DB_6M.T
    df_DB_6M.columns = ['6Month']

    df_DB_12M = df_DB_M[Col_12M].tail(1)
    df_DB_12M.columns = [indexs]
    df_DB_12M = df_DB_12M.T
    df_DB_12M.columns = ['12Month']

    df_DB_T = df_DB_M[Col_M].tail(1)
    df_DB_T.columns = [indexs]
    df_DB_T = df_DB_T.T
    df_DB_T.columns = ['Total']
    
    df_DB_Comment = pd.DataFrame(columns=['Description'],index=[indexs])
    
    df_DB_Comment['Description'].iloc[0] = 'S&P500'
    df_DB_Comment['Description'].iloc[1] = '선진국 주식'
    df_DB_Comment['Description'].iloc[2] = '신흥국 주식'
    df_DB_Comment['Description'].iloc[3] = '미국 정크본드'
    df_DB_Comment['Description'].iloc[4] = '미국 단기국채'
    df_DB_Comment['Description'].iloc[5] = '미국 중기국채'
    df_DB_Comment['Description'].iloc[6] = '미국 장기국채'
    df_DB_Comment['Description'].iloc[7] = '원자재'
    df_DB_Comment['Description'].iloc[8] = '원자재'
    df_DB_Comment['Description'].iloc[9] = '금'
    
    df_DB = pd.concat([df_DB_Comment,df_DB_1M,df_DB_3M,df_DB_6M,df_DB_12M,df_DB_T],axis=1)
    
    #df_DB_M['Date'] = df_DB_M["Date"].dt.strftime("%Y-%m-%d")
    df_DB_M = df_DB_M.set_index(keys=['Date'], inplace=False, drop=False)
    
    df_DB_Stocks = pd.DataFrame(columns=['Stocks'])
    df_DB_Stocks['Stocks'] = (df_DB_M['SPY_M'] + df_DB_M['EFA_M'] + df_DB_M['EEM_M'])/3

    df_DB_Bonds = pd.DataFrame(columns=['Bonds'])
    df_DB_Bonds['Bonds'] = (df_DB_M['AGG_M'] + df_DB_M['SHY_M'] + df_DB_M['IEF_M'] + df_DB_M['TLT_M'])/4

    df_DB_Comm = pd.DataFrame(columns=['Commodity'])
    df_DB_Comm['Commodity'] = (df_DB_M['DBC_M'] + df_DB_M['GSG_M'])/2
    
    df_DB_Gold = pd.DataFrame(columns=['Gold'])
    df_DB_Gold['Gold'] = df_DB_M['IAU_M']
      
    df_DB2 = pd.concat([df_DB_Stocks,df_DB_Bonds,df_DB_Comm,df_DB_Gold],axis=1)
    
    print(df_DB2)
    
    return df_DB, df_DB2

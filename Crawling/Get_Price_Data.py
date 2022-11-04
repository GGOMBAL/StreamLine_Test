import pandas_datareader as pdr
import pandas as pd
import numpy as np
import FinanceDataReader as fdr

from datetime import datetime, timedelta
#from Strategy_DAA import *

def get_yahoo_price_data(Universe, start_day, end_day):
    
    df_ALL = pd.DataFrame(columns=Universe)

    for ticker in Universe:
        df_ALL[ticker] = pdr.get_data_yahoo(ticker, start_day - timedelta(days=365), end_day)['Adj Close']  
        #df_ALL[ticker] = pdr.get_data_yahoo(ticker, start_day - timedelta(days=365), end_day)['Close']  
    
    df_ALL.round(2) 
    
    return df_ALL

def get_datareader_price_data(Universe, start_day, end_day):
    
    df_ALL = pd.DataFrame(columns=Universe)

    for ticker in Universe:

        #df_ALL[ticker] = fdr.DataReader(ticker, start_day, end_day)
        df = fdr.DataReader(ticker, start_day - timedelta(days=62), end_day)['Close']
        #df = df.drop(['Open'], axis=1)
        #df = df.drop(['High'], axis=1)
        #df = df.drop(['Low'], axis=1)
        #df = df.drop(['Volume'], axis=1)
        #df = df.drop(['Change'], axis=1)
        
        df_ALL[ticker] = df
    
    df_ALL.round(2)
    
    return df_ALL

def get_krx_price_data(Universe, start_day, end_day):
    df_ALL = pd.DataFrame(columns=Universe)

    df_ALL = pd.read_excel(r'QUANT_Input_KRX.xlsx', sheet_name='Sheet1',header= 0,index_col='일자',na_values = 'NaN')
    
    df_ALL.round(2)
    
    print(df_ALL)

    
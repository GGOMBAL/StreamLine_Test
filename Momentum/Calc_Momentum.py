import pandas_datareader as pdr
import pandas as pd
import numpy as np

from datetime import datetime, timedelta
#from Strategy_DAA import *

def get_momentum(x, df_ALL, universe):
    temp_list = [0 for i in range(len(x.index))]
    momentum = pd.Series(temp_list, index=x.index)

    try:
        before1 = df_ALL[x.name-timedelta(days=35):x.name-timedelta(days=30)].iloc[-1][universe]
        before3 = df_ALL[x.name-timedelta(days=95):x.name-timedelta(days=90)].iloc[-1][universe]        
        before6 = df_ALL[x.name-timedelta(days=185):x.name-timedelta(days=180)].iloc[-1][universe]        
        before12 = df_ALL[x.name-timedelta(days=370):x.name-timedelta(days=365)].iloc[-1][universe]

        momentum = round((12 * (x / before1 - 1) + 4 * (x / before3 - 1) + 2 * (x / before6 - 1) + (x / before12 - 1)),2)
    except:
        pass
   
    return round(momentum,3)

def get_acc_momentum(x, df_ALL, universe):
    
    temp_list = [0 for i in range(len(x.index))]
    momentum = pd.Series(temp_list, index=x.index)

    try:
        before1 = df_ALL[x.name-timedelta(days=35):x.name-timedelta(days=30)].iloc[-1][universe]
        before3 = df_ALL[x.name-timedelta(days=95):x.name-timedelta(days=90)].iloc[-1][universe]        
        before6 = df_ALL[x.name-timedelta(days=185):x.name-timedelta(days=180)].iloc[-1][universe]        

        momentum = (x / before1 - 1) + (x / before3 - 1) + (x / before6 - 1)
    except:
        pass

    return round(momentum,3)

def get_12m_momentum(x, df_ALL, universe):
    
    temp_list = [0 for i in range(len(x.index))]
    momentum = pd.Series(temp_list, index=x.index)

    try:
        before12 = df_ALL[x.name-timedelta(days=370):x.name-timedelta(days=365)].iloc[-1][universe]      

        momentum = x / before12 - 1
    except:
        pass

    return round(momentum,3)

def get_6m_momentum(x, df_ALL, universe):
    
    temp_list = [0 for i in range(len(x.index))]
    momentum = pd.Series(temp_list, index=x.index)

    try:
        before6 = df_ALL[x.name-timedelta(days=185):x.name-timedelta(days=180)].iloc[-1][universe]      

        momentum = x / before6 - 1
    except:
        pass

    return round(momentum,3)

def get_3m_momentum(x, df_ALL, universe):
    
    temp_list = [0 for i in range(len(x.index))]
    momentum = pd.Series(temp_list, index=x.index)

    try:
        before3 = df_ALL[x.name-timedelta(days=95):x.name-timedelta(days=90)].iloc[-1][universe]      

        momentum = x / before3 - 1
    except:
        pass

    return round(momentum,3)

def get_1m_momentum(x, df_ALL, universe):
    
    temp_list = [0 for i in range(len(x.index))]
    momentum = pd.Series(temp_list, index=x.index)

    try:
        before1 = df_ALL[x.name-timedelta(days=35):x.name-timedelta(days=30)].iloc[-1][universe]      

        momentum = x / before1 - 1
    except:
        pass

    return round(momentum,3)



import pandas_datareader as pdr
import pandas as pd
import numpy as np
import math

from datetime import datetime, timedelta
from Momentum.Calc_Momentum import *

from Crawling.Get_Price_Data import *
from AssetAllocation.CallTodaysAsset import *

def Current_Momentum(start_day, end_day, df_DB, Sample):

# Makeup Universe
    Universe = ['SPY','EFA','EEM','AGG','SHY','IEF','TLT','DBC','GSG','IAU']
    
    df_MOM = df_DB[Universe].copy()
# Calculate Momentum
    mom_col_list_1M = [col+'_1M' for col in df_MOM[Universe].columns]
    mom_col_list_3M = [col+'_3M' for col in df_MOM[Universe].columns]
    mom_col_list_6M = [col+'_6M' for col in df_MOM[Universe].columns]
    mom_col_list_12M = [col+'_12M' for col in df_MOM[Universe].columns]

    df_MOM[mom_col_list_1M] = df_MOM[Universe].apply(lambda x: get_1m_momentum(x, df_MOM, Universe), axis=1)
    df_MOM[mom_col_list_3M] = df_MOM[Universe].apply(lambda x: get_3m_momentum(x, df_MOM, Universe), axis=1)
    df_MOM[mom_col_list_6M] = df_MOM[Universe].apply(lambda x: get_6m_momentum(x, df_MOM, Universe), axis=1)
    df_MOM[mom_col_list_12M] = df_MOM[Universe].apply(lambda x: get_12m_momentum(x, df_MOM, Universe), axis=1)
    
    mom_col_list = [col+'_M' for col in df_MOM[Universe].columns]
    df_MOM[mom_col_list] = df_MOM[Universe].apply(lambda x: get_momentum(x, df_MOM, Universe), axis=1)
    
# Duration of backtest
    df_MOM = df_MOM[datetime(2015,1,1):end_day]

# Select end data of month
    #if Sample == 'Month':
    #    df_MOM = df_MOM.resample(rule='M').last()
    
    #df_MOM = df_MOM.drop(Universe, axis=1)
    
    return df_MOM.tail(360)


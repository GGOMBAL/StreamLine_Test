import pandas_datareader as pdr
import pandas as pd
import numpy as np
import math

from datetime import datetime, timedelta
from Crawling.Get_Price_Data import *

class BM:
    
    def get_BenchMark(start_day,end_day):

        Universe = ['SPY','QQQ','^KQ11','^KS11']

        df_BM = get_yahoo_price_data(Universe, start_day, end_day)

        df_BM = df_BM[start_day:end_day]

        total_month = len(df_BM)

        col_BM_list_P = [col+'_P' for col in df_BM.columns]
        col_BM_list_AP = [col+'_AP' for col in df_BM.columns]
        col_BM_list_LP = [col+'_LP' for col in df_BM.columns]
        col_BM_list_ALP = [col+'_ALP' for col in df_BM.columns]
        col_BM_list_BAL = [col+'_BAL' for col in df_BM.columns]
        col_BM_list_DD = [col+'_DD' for col in df_BM.columns]

        df_BM[col_BM_list_P] = df_BM.pct_change()
        df_BM[col_BM_list_AP] = (1+df_BM[col_BM_list_P]).cumprod()-1
        df_BM[col_BM_list_LP] = np.log(df_BM[col_BM_list_P]+1)
        df_BM[col_BM_list_ALP] = df_BM[col_BM_list_LP].cumsum()

        df_BM[col_BM_list_P] = df_BM[col_BM_list_P]*100
        df_BM[col_BM_list_AP] = df_BM[col_BM_list_AP]*100

        df_BM[col_BM_list_BAL] = (1+df_BM[col_BM_list_P]/100).cumprod()
        df_BM[col_BM_list_DD] = -(df_BM[col_BM_list_BAL].cummax() - df_BM[col_BM_list_BAL]) / df_BM[col_BM_list_BAL].cummax()

        df_BM[col_BM_list_BAL] = df_BM[col_BM_list_BAL]*100
        df_BM[col_BM_list_DD] = df_BM[col_BM_list_DD]*100

        #BM_CAGR = ((1+df_BM['^GSPC_AP'][-1]/100)**(1/(total_month/12)))-1

        #print('## BenchMark CAGR : ', round(BM_CAGR*100,2))
        #print('## BM MDD value : ', round(df_BM['^GSPC_DD'].min(),2))

        return df_BM

import pandas_datareader as pdr
import pandas as pd
import numpy as np
import math

from datetime import datetime, timedelta
from Momentum.Calc_Momentum import *
from Crawling.Get_Price_Data import *

# 주식: SPY(VTI 대체 가능) - 25%
# 현금: BIL(SHY 대체 가능) - 25%
# 금: GLD - 25%
# 장기국채: TLT(IEF 대체 가능) - 25%

def PP_LV_MAIN(start_day, end_day, df_DB, Sample):

# Makeup Universe
    Universe = ['SSO','SHY','GLD','TLT'] 
    
    df_PP = df_DB[Universe]
    df_PP.index = df_PP.index.values.astype('<M8[m]')

# Duration of backtest
    df_PP = df_PP[start_day:end_day]

# Select end data of month
    if Sample == 'Month':
        df_PP = df_PP.resample(rule='M').last()

    for i in range(len(Universe)):
        df_PP.rename(columns = {Universe[i]:'ASSET'+'{}'.format(i)}, inplace = True)

    col_list_P = [col+'_P' for col in df_PP.columns]
    df_PP[col_list_P] = df_PP.pct_change()
    df_PP[col_list_P] = df_PP[col_list_P]*100

# monthly profit & accumulated profit 
    df_PP = Cal_PP_Profit(df_PP,Universe)

    return df_PP

def Cal_PP_Profit(df_PP,Universe):
    
    Universe_Cnt = len(Universe)
    Initial_Balance = 100

    for j in range(Universe_Cnt):
        df_PP['ASSET'+'{}'.format(j)+'_BAL'] = 0
        df_PP['ASSET'+'{}'.format(j)+'_MDD'] = 1

    for i in range(len(df_PP)):
        
        date = df_PP.index[i]
        total_Bal = 0

# Check Rebalancing Date
        if date.day == 30 and date.month == 12:
            df_PP.loc[date,'REBAL_CHK'] = True
        else:
            df_PP.loc[date,'REBAL_CHK'] = False

# Calculate Balance
        for j in range(Universe_Cnt):
            if i==0:
                temp = Initial_Balance/Universe_Cnt
                df_PP.loc[date,'ASSET'+'{}'.format(j)+'_BAL'] = temp
            else:
                temp = (df_PP['ASSET'+'{}'.format(j)+'_BAL'].iloc[i-1] * (1 + df_PP['ASSET'+'{}'.format(j)+'_P'].iloc[i]/100))
                df_PP.loc[date,'ASSET'+'{}'.format(j)+'_BAL'] = temp
            
            total_Bal = total_Bal + (df_PP['ASSET'+'{}'.format(j)+'_BAL'].iloc[i])

# Calculate MDD       
        for j in range(Universe_Cnt):
            if i==0:
                df_PP.loc[date,'ASSET'+'{}'.format(j)+'_MDD'] = 0
            else:
                mdd = -(df_PP['ASSET'+'{}'.format(j)+'_BAL'].max() - df_PP['ASSET'+'{}'.format(j)+'_BAL'].iloc[i]) / df_PP['ASSET'+'{}'.format(j)+'_BAL'].max()
                df_PP.loc[date,'ASSET'+'{}'.format(j)+'_MDD'] = mdd*100

# Rebalancing..
        for j in range(Universe_Cnt):
            if ( df_PP['REBAL_CHK'].iloc[i] == True):
                df_PP.loc[date,'ASSET'+'{}'.format(j)+'_BAL'] = total_Bal / Universe_Cnt    
            else:pass

        df_PP.loc[date,'PP_BAL'] = total_Bal  
        
        df_PP = df_PP.assign(PP_DD=lambda x: -(df_PP['PP_BAL'].cummax() - df_PP['PP_BAL']) / df_PP['PP_BAL'].cummax())
        df_PP['PP_DD'] = df_PP['PP_DD'] * 100

    return  df_PP 

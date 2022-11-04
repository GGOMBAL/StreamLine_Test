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

def CP_MAIN(start_day, end_day, df_DB, Sample):

# Makeup Universe
    Universe = ['SPY','IEF'] 
    df_CP = df_DB[Universe]
    #df_CP = get_yahoo_price_data(Universe, start_day, end_day)
    #df_CP.index = df_CP.index.values.astype('<M8[m]')

# Duration of backtest
    df_CP = df_CP[start_day:end_day]

# Select end data of month
    if Sample == 'Month':
        df_CP = df_CP.resample(rule='M').last()

# Calculate profit
    for i in range(len(Universe)):
        df_CP.rename(columns = {Universe[i]:'ASSET'+'{}'.format(i)}, inplace = True)

    col_list_P = [col+'_P' for col in df_CP.columns]

    df_CP[col_list_P] = df_CP.pct_change()
    df_CP[col_list_P] = df_CP[col_list_P]*100

# monthly profit & accumulated profit 
    df_CP = Cal_CP_Profit(df_CP,Universe)

    return df_CP

def Cal_CP_Profit(df_CP,Universe):
    
    Universe_Cnt = len(Universe)
    Initial_Balance = 100

    for j in range(Universe_Cnt):
        df_CP['ASSET'+'{}'.format(j)+'_BAL'] = 0
        df_CP['ASSET'+'{}'.format(j)+'_MDD'] = 1

# 날짜별 데이터 계산을 위해 for 구문 사용
    for i in range(len(df_CP)):
        
        date = df_CP.index[i]
        total_Bal = 0

# Check Rebalancing Date
        if date.month == 12 and date.day == 31:
            df_CP.loc[date,'REBAL_CHK'] = True
        else:
            df_CP.loc[date,'REBAL_CHK'] = False

# Calculate Balance
        for j in range(Universe_Cnt):
            if i==0:
                temp = Initial_Balance/Universe_Cnt
                df_CP.loc[date,'ASSET'+'{}'.format(j)+'_BAL'] = temp
            else:
                temp = (df_CP['ASSET'+'{}'.format(j)+'_BAL'].iloc[i-1] * (1 + df_CP['ASSET'+'{}'.format(j)+'_P'].iloc[i]/100))
                df_CP.loc[date,'ASSET'+'{}'.format(j)+'_BAL'] = temp
            
            total_Bal = total_Bal + (df_CP['ASSET'+'{}'.format(j)+'_BAL'].iloc[i])

# Calculate MDD       
        for j in range(Universe_Cnt):
            if i==0:
                df_CP.loc[date,'ASSET'+'{}'.format(j)+'_MDD'] = 0
            else:
                mdd = -(df_CP['ASSET'+'{}'.format(j)+'_BAL'].max() - df_CP['ASSET'+'{}'.format(j)+'_BAL'].iloc[i]) / df_CP['ASSET'+'{}'.format(j)+'_BAL'].max()
                df_CP.loc[date,'ASSET'+'{}'.format(j)+'_MDD'] = mdd*100

# Rebalancing..
        for j in range(Universe_Cnt):
            if ( df_CP['REBAL_CHK'].iloc[i] == True):
                df_CP.loc[date,'ASSET'+'{}'.format(j)+'_BAL'] = total_Bal / Universe_Cnt    
            else:pass

        df_CP.loc[date,'CP_BAL'] = total_Bal  
        
        df_CP = df_CP.assign(CP_DD=lambda x: -(df_CP['CP_BAL'].cummax() - df_CP['CP_BAL']) / df_CP['CP_BAL'].cummax())
        df_CP['CP_DD'] = df_CP['CP_DD'] * 100

    return  df_CP 

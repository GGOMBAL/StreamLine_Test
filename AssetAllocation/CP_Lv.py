import pandas_datareader as pdr
import pandas as pd
import numpy as np
import math

from datetime import datetime, timedelta
from Momentum.Calc_Momentum import *
from Crawling.Get_Price_Data import *

# 주식: SSO(VTI 대체 가능) - 25%
# 현금: BIL(SHY 대체 가능) - 25%
# 금: GLD - 25%
# 장기국채: TLT(IEF 대체 가능) - 25%

def CP_LV_MAIN(start_day, end_day, df_DB, Sample):

# Makeup Universe
    Universe = ['SSO','IEF'] 
    df_CP = df_DB[Universe]
    #df_CP = get_yahoo_price_data(Universe, start_day, end_day)
    #df_CP.index = df_CP.index.values.astype('<M8[m]')

# Duration of backtest
    df_CP = df_CP[start_day:end_day]

# Select end data of month
    if Sample == 'Month':
        df_CP = df_CP.resample(rule='M').last()

# Calculate profit
    col_list_P = [col+'_P' for col in df_CP.columns]

    df_CP[col_list_P] = df_CP.pct_change()
    df_CP[col_list_P] = df_CP[col_list_P]*100

# monthly profit & accumulated profit 
    df_CP = Cal_CP_Profit(df_CP,Universe)

    return df_CP

def Cal_CP_Profit(df_CP,Universe):
    
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
        if i==0:
            temp = 100
            df_CP.loc[date,'SSO_BAL'] = temp*60/100
            df_CP.loc[date,'IEF_BAL'] = temp*40/100
        else:
            df_CP.loc[date,'SSO_BAL'] = (df_CP['SSO_BAL'].iloc[i-1] * (1 + df_CP['SSO_P'].iloc[i]/100))
            df_CP.loc[date,'IEF_BAL'] = (df_CP['IEF_BAL'].iloc[i-1] * (1 + df_CP['IEF_P'].iloc[i]/100))
        
        total_Bal = df_CP['SSO_BAL'].iloc[i] + df_CP['IEF_BAL'].iloc[i]

# Calculate MDD       
        if i==0:
            df_CP.loc[date,'SSO_MDD'] = 0
            df_CP.loc[date,'IEF_MDD'] = 0
        else:
            mdd = -(df_CP['SSO_BAL'].max() - df_CP['SSO_BAL'].iloc[i]) / df_CP['SSO_BAL'].max()
            df_CP.loc[date,'SSO_MDD'] = mdd*100

            mdd = -(df_CP['IEF_BAL'].max() - df_CP['IEF_BAL'].iloc[i]) / df_CP['IEF_BAL'].max()           
            df_CP.loc[date,'IEF_MDD'] = mdd*100

# Rebalancing..

        if ( df_CP['REBAL_CHK'].iloc[i] == True):
            df_CP.loc[date,'SSO_BAL'] = total_Bal *60/100
            df_CP.loc[date,'IEF_BAL'] = total_Bal *40/100
        else:pass

        df_CP.loc[date,'CP_BAL'] = total_Bal  
        
        dd = -(df_CP['CP_BAL'].max() - df_CP['CP_BAL'].iloc[i]) / df_CP['CP_BAL'].max()
        df_CP.loc[date,'CP_DD'] = dd*100

    return  df_CP 

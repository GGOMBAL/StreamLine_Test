import pandas_datareader as pdr
import pandas as pd
import numpy as np
import math

from datetime import datetime, timedelta
from Momentum.Calc_Momentum import *
from Crawling.Get_Price_Data import *
from AssetAllocation.CallTodaysAsset import *

# Defensive = ['SPY','VSS','TLT']

def ADM_MAIN(start_day, end_day, df_DB, Sample):

    # Makeup Universe
    Universe = ['SPY','VSS','TLT']
    #Universe = ['SSO','TNA','TLT','SPY','VSS']

    df_ADM = df_DB[Universe].copy()
    
# Calculate Momentum
    mom_col_list = [col+'_M' for col in df_ADM[Universe].columns]
    df_ADM[mom_col_list] = df_ADM[Universe].apply(lambda x: get_acc_momentum(x, df_ADM, Universe), axis=1)

# Duration of backtest
    df_ADM = df_ADM[start_day:end_day]

# Select end data of month
    if Sample == 'Month':
        df_ADM = df_ADM.resample(rule='M').last()

    col_list_P = [col+'_P' for col in df_ADM[Universe].columns]
    df_ADM[col_list_P] = df_ADM[Universe].pct_change()

    df_ADM[['ASSET1','PRICE','Position']]     = df_ADM.apply(lambda x: select_ADM_asset(x), axis=1)

# monthly profit & accumulated profit 
    df_ADM = Cal_ADM_Profit(df_ADM)

    ADM_T_List = ['ASSET1','Position']
    
    df_ADM_T = Call_AA_Today_2(df_ADM,'ADM',ADM_T_List)
    
    return df_ADM, df_ADM_T

def select_ADM_asset(x):
    
    asset = pd.Series([0,0,0], index=['ASSET1','PRICE','Position'])

    #Universe = ['SPY','VSS','TLT']

    if x['SPY_M'] > x['VSS_M']:

        if  x['SPY_M'] > 0:
            max_momentum = x['SPY_M']
        else:
            max_momentum = x['TLT_M']
        
        asset['Position'] = 'Offensive'     
    
    else :

        if  x['VSS_M'] > 0:
            max_momentum = x['VSS_M']
        else:
            max_momentum = x['TLT_M']
        
        asset['Position'] = 'Deffensive'

    asset['ASSET1'] = x[x == max_momentum].index[0][:3]
    asset['PRICE'] = x[asset['ASSET1']]   
     
    return asset


# monthly profit & accumulated profit 

def Cal_ADM_Profit(df_ADM):

    df_ADM['ADM_P'] = 0
    df_ADM['ADM_AP'] = 0
    df_ADM['ADM_LP'] = 0
    df_ADM['ADM_ALP'] = 0

    for i in range(len(df_ADM)):
    
        profit = 0
        log_profit = 0
        
        if i != 0:
            profit = df_ADM[df_ADM.iloc[i-1]['ASSET1'] + '_P'].iloc[i]

            log_profit = math.log(profit+1)
    
        df_ADM.loc[df_ADM.index[i], 'ADM_P'] = profit
        df_ADM.loc[df_ADM.index[i], 'ADM_AP'] = (1+df_ADM.loc[df_ADM.index[i-1], 'ADM_AP'])*(1+profit)-1
        df_ADM.loc[df_ADM.index[i], 'ADM_LP'] = log_profit
        df_ADM.loc[df_ADM.index[i], 'ADM_ALP'] = df_ADM.loc[df_ADM.index[i-1], 'ADM_ALP'] + log_profit

    df_ADM[['ADM_P', 'ADM_ALP']] = df_ADM[['ADM_P', 'ADM_ALP']] * 100

    df_ADM = df_ADM.assign(ADM_BAL=lambda x: (1+df_ADM['ADM_P']/100).cumprod())
    df_ADM = df_ADM.assign(ADM_DD=lambda x: -(df_ADM['ADM_BAL'].cummax() - df_ADM['ADM_BAL']) / df_ADM['ADM_BAL'].cummax())

    df_ADM['ADM_BAL'] = df_ADM['ADM_BAL'] * 100
    df_ADM['ADM_DD'] = df_ADM['ADM_DD'] * 100

    return  df_ADM 

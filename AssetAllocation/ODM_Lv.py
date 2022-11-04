import pandas_datareader as pdr
import pandas as pd
import numpy as np
import math

from datetime import datetime, timedelta
from Momentum.Calc_Momentum import *
from Crawling.Get_Price_Data import *
from AssetAllocation.CallTodaysAsset import *

# Defensive = ['SPY','EFA','BIL']

def ODM_LV_MAIN(start_day, end_day, df_DB, Sample):

    # Makeup Universe
    Universe = ['SPY','EFA','BIL','AGG','SSO','EFO']
    #Universe = ['SSO','EFO','BIL','AGG']

    df_ODM = df_DB[Universe].copy()

# Calculate Momentum
    mom_col_list = [col+'_M' for col in df_ODM[Universe].columns]
    df_ODM[mom_col_list] = df_ODM[Universe].apply(lambda x: get_12m_momentum(x, df_ODM, Universe), axis=1)

# Duration of backtest
    df_ODM = df_ODM[start_day:end_day]

# Select end data of month
    if Sample == 'Month':
        df_ODM = df_ODM.resample(rule='M').last()

    col_list_P = [col+'_P' for col in df_ODM[Universe].columns]
    df_ODM[col_list_P] = df_ODM[Universe].pct_change()

    df_ODM[['ASSET1','PRICE','Position']]     = df_ODM.apply(lambda x: select_ODM_asset(x), axis=1)

# monthly profit & accumulated profit 
    df_ODM = Cal_ODM_Profit(df_ODM)

    ODM_T_List = ['ASSET1','Position']
    
    df_ODM_T = Call_AA_Today_2(df_ODM,'ODM_LV',ODM_T_List)
    
    return df_ODM, df_ODM_T

def select_ODM_asset(x):
    
    asset = pd.Series([0,0,0], index=['ASSET1','PRICE','Position'])

    #Universe = ['SPY','VSS','TLT']

    if x['SPY_M'] > x['BIL_M']:

        if  x['SPY_M'] > x['EFA_M']:
            max_momentum = x['SSO_M'] #Leverage
        else:
            max_momentum = x['EFO_M'] #Leverage
        
        asset['Position'] = 'Offensive'     
    
    else :
        max_momentum = x['AGG_M']
        
        asset['Position'] = 'Deffensive'

    asset['ASSET1'] = x[x == max_momentum].index[0][:3]
    asset['PRICE'] = x[asset['ASSET1']]   
     
    return asset


# monthly profit & accumulated profit 

def Cal_ODM_Profit(df_ODM):

    df_ODM['ODM_P'] = 0

    for i in range(len(df_ODM)):
    
        profit = 0
        log_profit = 0
        
        if i != 0:
            profit = df_ODM[df_ODM.iloc[i-1]['ASSET1'] + '_P'].iloc[i]

            log_profit = math.log(profit+1)
    
        df_ODM.loc[df_ODM.index[i], 'ODM_P'] = profit

    df_ODM['ODM_P'] = df_ODM['ODM_P'] * 100

    df_ODM = df_ODM.assign(ODM_BAL=lambda x: (1+df_ODM['ODM_P']/100).cumprod())
    df_ODM = df_ODM.assign(ODM_DD=lambda x: -(df_ODM['ODM_BAL'].cummax() - df_ODM['ODM_BAL']) / df_ODM['ODM_BAL'].cummax())

    df_ODM['ODM_BAL'] = df_ODM['ODM_BAL'] * 100
    df_ODM['ODM_DD'] = df_ODM['ODM_DD'] * 100

    return  df_ODM 

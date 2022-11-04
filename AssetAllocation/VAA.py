import pandas_datareader as pdr
import pandas as pd
import numpy as np
import math

from datetime import datetime, timedelta
from Momentum.Calc_Momentum import *
from Crawling.Get_Price_Data import *
from AssetAllocation.CallTodaysAsset import *

# Original Asset List
# Offensive = ['SPY','IWM','QQQ','VGK','EWJ','VWO','VNQ','GSG','GLD','TLT','HYG','LQD']
# Offensive = ['SPY','IWM','QQQ','VGK','EWJ','VWO','VNQ','GSG','GLD','TLT','HYG']
# Defensive = ['SHV','IEF','LQD','BND']

# Leverage Asset List
# Offensive = ['SSO','QLD','UWM','VGK','EWJ','VWO','VNQ','GSG','GLD','TLT','HYG','LQD']
# Defensive = ['SHV','IEF','LQD','BND']
# Defensive(Short) = ['SH','PSQ','RWM','BND']

# 연금계좌 Asset List
# Offensive = ['379800.KS', '379810.KS', '280930.KS', '132030.KS', '304660.KS', '182490.KS', '195930.KS', '241180.KS', '181480.KS', '291890.KS', '218420.KS']
# Defensive = ['214980.KS', '114460.KS', '136340.KS']


def VAA_MAIN(start_day, end_day, df_DB, Sample):

    # Makeup Universe
    Offensive = ['SPY','VEA','EEM','AGG'] 
    #Offensive = ['SSO','EFO','EET','AGG']
    Defensive = ['SHY','IEF','LQD']

    Universe = Offensive + Defensive

    df_VAA = df_DB[Universe].copy()
# Calculate Momentum
    mom_col_list_Off = [col+'_M' for col in df_VAA[Offensive].columns]
    mom_col_list_Def = [col+'_M' for col in df_VAA[Defensive].columns]
    mom_col_list = mom_col_list_Off + mom_col_list_Def

    df_VAA[mom_col_list] = df_VAA[Universe].apply(lambda x: get_momentum(x, df_VAA, Universe), axis=1)

# Duration of backtest
    df_VAA = df_VAA[start_day:end_day]

# Select end data of month
    if Sample == 'Month':
        df_VAA = df_VAA.resample(rule='M').last()

    col_list_P = [col+'_P' for col in df_VAA[Universe].columns]
    df_VAA[col_list_P] = df_VAA[Universe].pct_change()

    df_VAA[['ASSET1','PRICE1','Position']]     = df_VAA.apply(lambda x: select_VAA_asset(x), axis=1)

# monthly profit & accumulated profit 
    df_VAA = Cal_VAA_Profit(df_VAA)
    
    VAA_T_List = ['ASSET1','Position']
    
    df_VAA_T = Call_AA_Today_2(df_VAA,'VAA',VAA_T_List)
    
    return df_VAA, df_VAA_T

def select_VAA_asset(x):
    
    asset = pd.Series([0,0,0], index=['ASSET1','PRICE1','Position'])

    #Offensive = ['SSO','EFO','EET','AGG']

    if x['SPY_M'] > 0 and x['VEA_M'] > 0 and x['EEM_M'] > 0 and x['AGG_M'] > 0:
        max_momentum = max(x['SPY_M'],x['VEA_M'],x['EEM_M'],x['AGG_M'])
        asset['Position'] = 'Offensive'     
    
    else :
        max_momentum = max(x['LQD_M'],x['SHY_M'],x['IEF_M'])
        asset['Position'] = 'Deffensive'

    asset['ASSET1'] = x[x == max_momentum].index[0][:3]
    asset['PRICE1'] = x[asset['ASSET1']]   
     
    return asset


# monthly profit & accumulated profit 

def Cal_VAA_Profit(df_VAA):

    df_VAA['VAA_P'] = 0
    df_VAA['VAA_AP'] = 0
    df_VAA['VAA_LP'] = 0
    df_VAA['VAA_ALP'] = 0

    for i in range(len(df_VAA)):
    
        profit = 0
        log_profit = 0
        
        if i != 0:
            profit = df_VAA[df_VAA.iloc[i-1]['ASSET1'] + '_P'].iloc[i]

            log_profit = math.log(profit+1)
    
        df_VAA.loc[df_VAA.index[i], 'VAA_P'] = profit
        df_VAA.loc[df_VAA.index[i], 'VAA_AP'] = (1+df_VAA.loc[df_VAA.index[i-1], 'VAA_AP'])*(1+profit)-1
        df_VAA.loc[df_VAA.index[i], 'VAA_LP'] = log_profit
        df_VAA.loc[df_VAA.index[i], 'VAA_ALP'] = df_VAA.loc[df_VAA.index[i-1], 'VAA_ALP'] + log_profit

    df_VAA[['VAA_P', 'VAA_AP']] = df_VAA[['VAA_P', 'VAA_AP']] * 100

    df_VAA = df_VAA.assign(VAA_BAL=lambda x: (1+df_VAA['VAA_P']/100).cumprod())
    df_VAA = df_VAA.assign(VAA_DD=lambda x: -(df_VAA['VAA_BAL'].cummax() - df_VAA['VAA_BAL']) / df_VAA['VAA_BAL'].cummax())

    df_VAA['VAA_BAL'] = df_VAA['VAA_BAL'] * 100
    df_VAA['VAA_DD'] = df_VAA['VAA_DD'] * 100

    return  df_VAA 

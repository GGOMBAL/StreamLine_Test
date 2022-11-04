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

# Makeup Universe
#Offensive = ['SSO','QLD','UWM','VGK','EWJ','VWO','VNQ','GSG','GLD','TLT','HYG','LQD']

def DAA_MAIN(start_day, end_day, df_DB, Sample):

    Offensive = ['SPY','IWM','QQQ','VGK','EWJ','VWO','VNQ','GSG','GLD','TLT','HYG','LQD']
    Defensive = ['SHV','IEF','UST','BND']

    Universe = Offensive + Defensive

    #df_DAA = get_yahoo_price_data(Universe, start_day, end_day)
    
    df_DAA = df_DB[Universe].copy()
    # Calculate Momentum
    mom_col_list_Off = [col+'_M' for col in df_DAA[Offensive].columns]
    mom_col_list_Def = [col+'_M' for col in df_DAA[Defensive].columns]
    mom_col_list = mom_col_list_Off + mom_col_list_Def

    df_DAA[mom_col_list] = df_DAA[Universe].apply(lambda x: get_momentum(x, df_DAA, Universe), axis=1)

# Duration of backtest
    df_DAA = df_DAA[start_day:end_day]

# Select end data of month
    if Sample == 'Month':
        df_DAA = df_DAA.resample(rule='M').last()

    col_list_P = [col+'_P' for col in df_DAA[Universe].columns]
    df_DAA[col_list_P] = df_DAA[Universe].pct_change()

# Select asset and price
    df_DAA[['ASSET1','PRICE1','ASSET2','PRICE2','ASSET3','PRICE3','ASSET4','PRICE4','Position']]     = df_DAA.apply(lambda x: select_DAA_asset(x, mom_col_list_Off, mom_col_list_Def), axis=1)

# monthly profit & accumulated profit 
    df_DAA = Cal_DAA_Profit(df_DAA)

    DAA_T_List = ['ASSET1','ASSET2','ASSET3','ASSET4','Position']
    
    df_DAA_T = Call_AA_Today_2(df_DAA,'DAA',DAA_T_List)
    
    return df_DAA, df_DAA_T

def select_DAA_asset(x, mom_col_list_Off, mom_col_list_Def):
    
    asset = pd.Series([0,0,0,0,0,0,0,0,0], index=['DAA_ASSET1','DAA_PRICE1','DAA_ASSET2','DAA_PRICE2','DAA_ASSET3','DAA_PRICE3','DAA_ASSET4','DAA_PRICE4','Position'])

    momentum1 = None
    momentum2 = None
    
    # DAA strategy

    if x['VWO_M'] > 0 and x['BND_M'] > 0:
        momentum_sort_Off = x[mom_col_list_Off].sort_values(ascending=False)

        momentum1 = momentum_sort_Off[0]
        momentum2 = momentum_sort_Off[1]
        momentum3 = momentum_sort_Off[2]
        momentum4 = momentum_sort_Off[3]

        asset['DAA_ASSET1'] = x[x == momentum1].index[0][:3]
        #asset['DAA_PRICE1'] = x[asset['DAA_ASSET1']] 
        asset['DAA_ASSET2'] = x[x == momentum2].index[0][:3]
        #asset['DAA_PRICE2'] = x[asset['DAA_ASSET2']]
        asset['DAA_ASSET3'] = x[x == momentum3].index[0][:3]
        #asset['DAA_PRICE3'] = x[asset['DAA_ASSET3']]
        asset['DAA_ASSET4'] = x[x == momentum4].index[0][:3]
        #asset['DAA_PRICE4'] = x[asset['DAA_ASSET4']]
        
        asset['Position'] = 'Offensive'

    elif x['VWO_M'] > 0 or x['BND_M'] > 0:
        momentum_sort_Off = x[mom_col_list_Off].sort_values(ascending=False)
        momentum_sort_Def = x[mom_col_list_Def].sort_values(ascending=False)

        momentum1 = momentum_sort_Off[0]
        momentum2 = momentum_sort_Off[1]
        momentum3 = momentum_sort_Def[0]
        momentum4 = momentum_sort_Def[0]

        asset['DAA_ASSET1'] = x[x == momentum1].index[0][:3]
        #asset['DAA_PRICE1'] = x[asset['DAA_ASSET1']] 
        asset['DAA_ASSET2'] = x[x == momentum2].index[0][:3]
        #asset['DAA_PRICE2'] = x[asset['DAA_ASSET2']]
        asset['DAA_ASSET3'] = x[x == momentum3].index[0][:3]
        #asset['DAA_PRICE3'] = x[asset['DAA_ASSET3']]
        asset['DAA_ASSET4'] = x[x == momentum4].index[0][:3]
        #asset['DAA_PRICE4'] = x[asset['DAA_ASSET4']]

        asset['Position'] = 'Neutrality'
    else :
        momentum_sort_Def = x[mom_col_list_Def].sort_values(ascending=False)

        momentum1 = momentum_sort_Def[0]
        momentum2 = momentum_sort_Def[0]
        momentum3 = momentum_sort_Def[0]
        momentum4 = momentum_sort_Def[0]

        asset['DAA_ASSET1'] = x[x == momentum1].index[0][:3]
        #asset['DAA_PRICE1'] = x[asset['DAA_ASSET1']] 
        asset['DAA_ASSET2'] = x[x == momentum2].index[0][:3]
        #asset['DAA_PRICE2'] = x[asset['DAA_ASSET2']]
        asset['DAA_ASSET3'] = x[x == momentum3].index[0][:3]
        #asset['DAA_PRICE3'] = x[asset['DAA_ASSET3']]
        asset['DAA_ASSET4'] = x[x == momentum4].index[0][:3]
        #asset['DAA_PRICE4'] = x[asset['DAA_ASSET4']]      
    
        asset['Position'] = 'Deffensive'
    return asset

# monthly profit & accumulated profit 

def Cal_DAA_Profit(df_DAA):

    df_DAA['DAA_P'] = 0
    df_DAA['DAA_AP'] = 0
    df_DAA['DAA_LP'] = 0
    df_DAA['DAA_ALP'] = 0

    for i in range(len(df_DAA)):
    
        profit = 0
        log_profit = 0
        
        if i != 0:
            profit = (
               df_DAA[df_DAA.iloc[i-1]['ASSET1'] + '_P'].iloc[i]
             + df_DAA[df_DAA.iloc[i-1]['ASSET2'] + '_P'].iloc[i]
             + df_DAA[df_DAA.iloc[i-1]['ASSET3'] + '_P'].iloc[i]
             + df_DAA[df_DAA.iloc[i-1]['ASSET4'] + '_P'].iloc[i]) / 4

            log_profit = math.log(profit+1)
    
        df_DAA.loc[df_DAA.index[i], 'DAA_P'] = profit
        df_DAA.loc[df_DAA.index[i], 'DAA_AP'] = (1+df_DAA.loc[df_DAA.index[i-1], 'DAA_AP'])*(1+profit)-1
        df_DAA.loc[df_DAA.index[i], 'DAA_LP'] = log_profit
        df_DAA.loc[df_DAA.index[i], 'DAA_ALP'] = df_DAA.loc[df_DAA.index[i-1], 'DAA_ALP'] + log_profit

    df_DAA[['DAA_P', 'DAA_AP']] = df_DAA[['DAA_P', 'DAA_AP']] * 100

    df_DAA = df_DAA.assign(DAA_BAL=lambda x: (1+df_DAA['DAA_P']/100).cumprod())
    df_DAA = df_DAA.assign(DAA_DD=lambda x: -(df_DAA['DAA_BAL'].cummax() - df_DAA['DAA_BAL']) / df_DAA['DAA_BAL'].cummax())

    df_DAA['DAA_BAL'] = df_DAA['DAA_BAL'] * 100
    df_DAA['DAA_DD'] = df_DAA['DAA_DD'] * 100

    #risky_month = len(df_DAA[df_DAA['ASSET1'].isin(Offensive)])
    #cash_month = len(df_DAA[df_DAA['ASSET1'].isin(Defensive)])

    #print("- In", total_month, "Month, Offensive Asset choice :", risky_month, "Month")
    #print("- In", total_month, "Month, Defensive Asset choice :", cash_month, "Month")

    return  df_DAA 

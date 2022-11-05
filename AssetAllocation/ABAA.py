import pandas_datareader as pdr
import pandas as pd
import numpy as np
import math

from datetime import datetime, timedelta
from Momentum.Calc_Momentum import *
from Crawling.Get_Price_Data import *
from AssetAllocation.CallTodaysAsset import *

# Original Asset List
# Offensive = ['SPY','QQQ','IWM','GLD','TLT','HYG','VGK','EWJ','VNQ','EEM','GSG']
# Defensive = ['SHV','IEF','LQD','BND']

# Leverage Asset List

# 연금계좌 Asset List

def ABAA_MAIN(start_day, end_day, df_DB, Sample):

    Offensive = ['QQQ','VWO','VEA','BND']
    Kanaria = ['SPY','VWO','VEA','BND']
    #Kanaria = ['SPY','EFA','EEM','AGG']
    Defensive = ['BIL','IEF','TLT','LQD','TIP','BND','DBC']

    df_BAA_O = df_DB[Offensive].copy()
    df_BAA_D = df_DB[Defensive].copy()
    df_BAA_K = df_DB[Kanaria].copy()
    
    df_BAA_O.index = df_BAA_O.index.values.astype('<M8[m]')
    df_BAA_D.index = df_BAA_D.index.values.astype('<M8[m]')
    df_BAA_K.index = df_BAA_K.index.values.astype('<M8[m]')
    
    for i in range(len(Offensive)):
        df_BAA_O.rename(columns = {Offensive[i]:'Offensive'+'{}'.format(i)}, inplace = True)
    
    Offensive_renamed = list(df_BAA_O.columns)
    
    for i in range(len(Defensive)):
        df_BAA_D.rename(columns = {Defensive[i]:'Defensive'+'{}'.format(i)}, inplace = True)

    Defensive_renamed = list(df_BAA_D.columns)
    
    for i in range(len(Kanaria)):
        df_BAA_K.rename(columns = {Kanaria[i]:'Kanaria'+'{}'.format(i)}, inplace = True)

    Kanaria_renamed = list(df_BAA_K.columns)
    
    Universe = Offensive_renamed + Defensive_renamed + Kanaria_renamed
    
    # Calculate Momentum
    mom_col_list_Off = [col+'_M' for col in df_BAA_O[Offensive_renamed].columns]
    mom_col_list_Kan = [col+'_M' for col in df_BAA_K[Kanaria_renamed].columns]
    mva_col_list_Def_Temp = [col+'_TEMP' for col in df_BAA_D[Defensive_renamed].columns]
    mva_col_list_Def = [col+'_MA' for col in df_BAA_D[Defensive_renamed].columns]

    df_BAA_O[mom_col_list_Off] = df_BAA_O.apply(lambda x: get_momentum(x, df_BAA_O, Offensive_renamed), axis=1)
    df_BAA_K[mom_col_list_Kan] = df_BAA_K.apply(lambda x: get_momentum(x, df_BAA_K, Kanaria_renamed), axis=1)   
    df_BAA_D[mva_col_list_Def_Temp] = df_BAA_D[Defensive_renamed].rolling(window=365,min_periods=1).mean()
    
    for i in range(len(df_BAA_D)):
        for j in range(0,7):
           
            if i !=0:
                Current_val = df_BAA_D['Defensive'+'{}'.format(j)].iloc[i]
                Avarage_val = df_BAA_D['Defensive'+'{}'.format(j)+'_TEMP'].iloc[i]
                temp = float(Current_val) - float(Avarage_val)

                df_BAA_D.loc[df_BAA_D.index[i], 'Defensive'+'{}'.format(j)+'_MA'] = temp
            else:
                df_BAA_D.loc[df_BAA_D.index[i], 'Defensive'+'{}'.format(j)+'_MA'] = 0
            
    df_BAA = df_BAA_O.join(df_BAA_D)
    df_BAA = df_BAA.join(df_BAA_K)
    
# Duration of backtest
    df_BAA = df_BAA[start_day:end_day]

# Select end data of month
    if Sample == 'Month':
        df_BAA = df_BAA.resample(rule='M').last()

    col_list_P = [col+'_P' for col in df_BAA[Universe].columns]
    df_BAA[col_list_P] = df_BAA[Universe].pct_change()   
    
    df_BAA['CASH'] = 0
    df_BAA['CASH_P'] = 0
        
# Select asset and price
    df_BAA[['ASSET1','ASSET2','ASSET3','MOMENTUM1','MOMENTUM2','MOMENTUM3','Position']] = \
        df_BAA.apply(lambda x: select_ASSET(x, mom_col_list_Off, mva_col_list_Def), axis=1)

    df_BAA.to_excel('Report/AA/ABAA.xlsx')
        
# monthly profit & accumulated profit 
    df_BAA = Cal_BAA_Profit(df_BAA)

    BAA_T_List = ['ASSET1','ASSET2','ASSET3','Position']
    
    df_BAA_T = Call_AA_Today(df_BAA,Offensive,Defensive,'ABAA',BAA_T_List)
    
    return df_BAA, df_BAA_T

def select_ASSET(x, mom_col_list_Off, mva_col_list_Def):
    
    asset = pd.Series([0,0,0,0,0,0,0], index=['ASSET1','ASSET2','ASSET3','MOMENTUM1','MOMENTUM2','MOMENTUM3','Position'])

    momentum1 = None
    momentum2 = None
    momentum3 = None

    temp = []
    
    # BAA strategy ['SPY','VWO','VEA','BND']

    if x['Kanaria0_M'] > 0 and x['Kanaria1_M'] > 0 and x['Kanaria2_M'] > 0 and x['Kanaria3_M'] > 0:
        momentum_sort_Off = x[mom_col_list_Off].sort_values(ascending=False)

        momentum1 = momentum_sort_Off[0]
        momentum2 = momentum_sort_Off[0]
        momentum3 = momentum_sort_Off[0]
               
        temp = x[x == momentum1].index[0].split('_')
        asset['ASSET1'] = temp[0]
        temp = x[x == momentum2].index[0].split('_')
        asset['ASSET2'] = temp[0]
        temp = x[x == momentum3].index[0].split('_')
        asset['ASSET3'] = temp[0]  
             
        asset['MOMENTUM1'] = momentum1
        asset['MOMENTUM2'] = momentum2
        asset['MOMENTUM3'] = momentum3
        
        asset['Position'] = 'Offensive'

    else :
        momentum_sort_Def = x[mva_col_list_Def].sort_values(ascending=False)

        momentum1 = momentum_sort_Def[0]
        momentum2 = momentum_sort_Def[1]
        momentum3 = momentum_sort_Def[2]

        if momentum1 > 0:
            temp = x[x == momentum1].index[0].split('_')
            asset['ASSET1'] = temp[0]
        else:
            asset['ASSET1'] = 'CASH'
        if momentum2 > 0:
            temp = x[x == momentum2].index[0].split('_')
            asset['ASSET2'] = temp[0]
        else:
            asset['ASSET2'] = 'CASH'
        if momentum3 > 0:    
            temp = x[x == momentum3].index[0].split('_')
            asset['ASSET3'] = temp[0]
        else:
            asset['ASSET3'] = 'CASH'
        
        asset['MOMENTUM1'] = momentum1
        asset['MOMENTUM2'] = momentum2
        asset['MOMENTUM3'] = momentum3
        
        asset['Position'] = 'Deffensive'

    return asset

# monthly profit & accumulated profit 

def Cal_BAA_Profit(df_BAA):

    df_BAA['BAA_P'] = 0
    profit = 0
    
    for i in range(len(df_BAA)):
    
        if i != 0:
            if df_BAA['Position'].iloc[i] == 'Offensive':
                
                profit = (
                   df_BAA[df_BAA.iloc[i-1]['ASSET1'] + '_P'].iloc[i]
                 + df_BAA[df_BAA.iloc[i-1]['ASSET2'] + '_P'].iloc[i]
                 + df_BAA[df_BAA.iloc[i-1]['ASSET3'] + '_P'].iloc[i]) / 3   
            else:
                    
                profit = (
                   df_BAA[df_BAA.iloc[i-1]['ASSET1'] + '_P'].iloc[i]
                 + df_BAA[df_BAA.iloc[i-1]['ASSET2'] + '_P'].iloc[i]
                 + df_BAA[df_BAA.iloc[i-1]['ASSET3'] + '_P'].iloc[i]) / 3               
    
        df_BAA.loc[df_BAA.index[i], 'BAA_P'] = profit

    df_BAA[['BAA_P']] = df_BAA[['BAA_P']] * 100

    df_BAA = df_BAA.assign(ABAA_BAL=lambda x: (1+df_BAA['BAA_P']/100).cumprod())
    df_BAA = df_BAA.assign(ABAA_DD=lambda x: -(df_BAA['ABAA_BAL'].cummax() - df_BAA['ABAA_BAL']) / df_BAA['ABAA_BAL'].cummax())

    df_BAA['ABAA_BAL'] = df_BAA['ABAA_BAL'] * 100
    df_BAA['ABAA_DD'] = df_BAA['ABAA_DD'] * 100

    return  df_BAA 

import pandas_datareader as pdr
import pandas as pd
import numpy as np
import math

from datetime import datetime, timedelta
from Crawling.Get_Price_Data import *

def Asset_Rebalancing(Universe,Initial_Balance,start_day,end_day,Rebalancing,Fee):

    Universe_Cnt = len(Universe)
        
    df_ALL = get_datareader_price_data(Universe, start_day, end_day)

    df_ALL.index = df_ALL.index.values.astype('<M8[m]')
    
# Select end data of month
    #df_ALL = df_ALL.resample(rule='M').last()

# Calculate Profit & log Profit
    for i in range(len(Universe)):
        df_ALL.rename(columns = {Universe[i]:'ASSET'+'{}'.format(i)}, inplace = True)

    col_list_P = [col+'_P' for col in df_ALL.columns]
    col_list_AP = [col+'_AP' for col in df_ALL.columns]

    df_ALL[col_list_P] = df_ALL.pct_change()
    df_ALL[col_list_AP] = (1+df_ALL[col_list_P]).cumprod()-1

    df_ALL[col_list_P] = df_ALL[col_list_P]*100
    df_ALL[col_list_AP] = df_ALL[col_list_AP]*100

# Duration of backtest
    df_ALL = df_ALL[start_day:end_day]

# Portpolio Rebalancing
    df_ALL['ASSET_BAL'] = Initial_Balance
    
    for j in range(Universe_Cnt):
        df_ALL['ASSET'+'{}'.format(j)+'_BAL'] = 0
        df_ALL['ASSET'+'{}'.format(j)+'_MDD'] = 1

    for i in range(len(df_ALL)):

        date = df_ALL.index[i]
        temp = 0
        total_Bal = 0
# Check Rebalancing Date
        if (date.day == 1):
            if (Rebalancing == True):
                df_ALL.loc[date,'REBAL_CHK'] = True
            else:
                df_ALL.loc[date,'REBAL_CHK'] = False
        else:
            df_ALL.loc[date,'REBAL_CHK'] = False

# Calculate Balance
        for j in range(Universe_Cnt):
            if i==0:
                temp = ( (Initial_Balance/Universe_Cnt) * (1 + df_ALL['ASSET'+'{}'.format(j)+'_P'].iloc[i]/100))
                df_ALL.loc[date,'ASSET'+'{}'.format(j)+'_BAL'] = temp
            else:
                temp = (df_ALL['ASSET'+'{}'.format(j)+'_BAL'].iloc[i-1] * (1 + df_ALL['ASSET'+'{}'.format(j)+'_P'].iloc[i]/100))
                df_ALL.loc[date,'ASSET'+'{}'.format(j)+'_BAL'] = temp
            
            total_Bal = total_Bal + (df_ALL['ASSET'+'{}'.format(j)+'_BAL'].iloc[i])
                
        df_ALL.loc[date,'ASSET_BAL'] = total_Bal
            
# Calculate MDD       
        for j in range(Universe_Cnt):
            if i==0:
                df_ALL.loc[date,'ASSET'+'{}'.format(j)+'_MDD'] = 0
            else:
                mdd = -(df_ALL['ASSET'+'{}'.format(j)+'_BAL'].max() - df_ALL['ASSET'+'{}'.format(j)+'_BAL'].iloc[i]) / df_ALL['ASSET'+'{}'.format(j)+'_BAL'].max()
                df_ALL.loc[date,'ASSET'+'{}'.format(j)+'_MDD'] = mdd*100

# Monthly Rebalancing..
        for j in range(Universe_Cnt):
            if ( df_ALL['REBAL_CHK'].iloc[i] == True):
                df_ALL.loc[date,'ASSET'+'{}'.format(j)+'_BAL'] = (total_Bal*((100-Fee)/100)) / Universe_Cnt
            else:
                pass

    balance = (df_ALL['ASSET_BAL'].iloc[-1])
# Rebalancing..50:50
#        if i==0:
#            df_ALL.loc[date,'CASH'] = 0
#            df_ALL.loc[date,'STOCK_BAL'] = total_Bal
#        else:
#            Total_Balance = total_Bal + df_ALL['CASH'].iloc[i-1]
#
#            if ( df_ALL['REBAL_CHK'].iloc[i] == True):
#
#                if df_ALL['PBR'].iloc[i] < 1.1 or df_ALL['KOSPI_M'].iloc[i] > 0:
#                    df_ALL.loc[date,'STOCK_BAL'] = Total_Balance
#                    df_ALL.loc[date,'CASH'] = 0
#                elif df_ALL['PBR'].iloc[i] < 1.3:
#                    df_ALL.loc[date,'STOCK_BAL'] = Total_Balance*0.8
#                    df_ALL.loc[date,'CASH'] = Total_Balance*0.2
#                elif df_ALL['PBR'].iloc[i] < 1.4:
#                    df_ALL.loc[date,'STOCK_BAL'] = Total_Balance*0.6
#                    df_ALL.loc[date,'CASH'] = Total_Balance*0.4
#                elif df_ALL['PBR'].iloc[i] < 1.5:
#                    df_ALL.loc[date,'STOCK_BAL'] = Total_Balance*0.4
#                    df_ALL.loc[date,'CASH'] = Total_Balance*0.6
#                else:
#                    df_ALL.loc[date,'STOCK_BAL'] = Total_Balance*0.2
#                    df_ALL.loc[date,'CASH'] = Total_Balance*0.8
#
#            else:
#                df_ALL.loc[date,'STOCK_BAL'] = total_Bal
#                df_ALL.loc[date,'CASH'] = df_ALL['CASH'].iloc[i-1]
#
#        df_ALL.loc[date,'ASSET_BAL'] = df_ALL['STOCK_BAL'].iloc[i] + df_ALL['CASH'].iloc[i]
#                
#        for j in range(Universe_Cnt):
#    
#            df_ALL.loc[date,'ASSET'+'{}'.format(j)+'_BAL'] = (df_ALL['STOCK_BAL'].iloc[i]*((100-Fee)/100)) / Universe_Cnt    
#
#    
    
    #CAGR = ((1+Accumulated_Profit/100)**(1/((start_day - end_day)/365)))-1
    #print('\n## CAGR : ', round(CAGR*100,2))
    
    
    df_ALL['ASSET_P'] = df_ALL['ASSET_BAL'].pct_change()
    df_ALL['ASSET_P'] = df_ALL['ASSET_P']*100
    
    return df_ALL, balance
    

import pandas_datareader as pdr
import pandas as pd
import numpy as np
import math
import FinanceDataReader as fdr

from datetime import datetime, timedelta
from Momentum.Calc_Momentum import *

def Strategy_Mix(df_QUANT1, df_QUANT2):

    df_QUANT_ALL = df_QUANT1.join(df_QUANT2)
    df_QUANT_ALL.merge(left = df_QUANT1 , right = df_QUANT2, how = "inner", on = "Date")
    
    print(df_QUANT_ALL.tail())
        
    #df_QUANT1 = pd.read_excel(r'Quantking\QUANT_Input_4Q.xlsx', sheet_name='Sheet1',header= 0,index_col='Date',na_values = 'NaN')
    #df_QUANT1 = Cal_Profit(df_QUANT1)

    #df_QUANT2 = pd.read_excel(r'Quantking\QUANT_Input_1Y.xlsx', sheet_name='Sheet1',header= 0,index_col='Date',na_values = 'NaN')
    #df_QUANT2 = Cal_Profit(df_QUANT2)

    #df_QUANT3 = pd.read_excel(r'Quantking\QUANT_Input_SUM.xlsx', sheet_name='Sheet1',header= 0,index_col='Date',na_values = 'NaN')
    df_QUANT_ALL = Cal_Profit(df_QUANT_ALL)

    return 

def Cal_Profit(df_QUANT):

    for i in range(len(df_QUANT)):
        
        total_Bal = 0
        
        total_Bal = (df_QUANT['QT1_BAL'].iloc[i] + df_QUANT['QT1_BAL'].iloc[i])/2
        
        df_QUANT.loc[df_QUANT.index[i], 'QT_BAL'] = total_Bal
        
    return  df_QUANT 
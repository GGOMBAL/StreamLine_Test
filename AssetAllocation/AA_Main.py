import pandas_datareader as pdr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager as fm
import quantstats as qs
import seaborn as sns
import math
import os
import time
from IPython.display import clear_output

from datetime import datetime, timedelta
from Momentum.Calc_Momentum import *

from AssetAllocation.DAA import *
from AssetAllocation.DAA_Lv import *
from AssetAllocation.VAA import *
from AssetAllocation.VAA_Lv import *
from AssetAllocation.BAA import *
from AssetAllocation.ABAA import *
from AssetAllocation.BAA_Lv import *
from AssetAllocation.ABAA_Lv import *
from AssetAllocation.ADM import *
from AssetAllocation.ADM_Lv import *
from AssetAllocation.PP import *
from AssetAllocation.PP_Lv import *
from AssetAllocation.CP import *
from AssetAllocation.CP_Lv import *
from AssetAllocation.ODM import *
from AssetAllocation.ODM_Lv import *
from DB.db_helper import *

#from BackTest_Main import start_day, end_day

#class BackTest():
#    def __init__(self):
#        self.strategy_name = "BackTest"
#        
#        self.AA = self.AA_Main()
#        global CP, PP, DAA , VAA , BAA , ABAA, ADM ,ODM
#        
#    os.system('cls' if os.name == 'nt' else 'clear')
#    pd.options.display.float_format = '{:.4f}'.format
#    pd.set_option('display.max_columns', None)
global CP, PP, DAA , VAA , BAA , ABAA, ADM ,ODM, Plot_Ena
         
class AA:
    
    def AA_Main(start_day,end_day):
    ## 백테스트 기간 설정 ##
        Sampling = 'Month'
        clear_output(wait=True)

        Plot_Ena = False
        
        CP = True
        PP = True
        DAA = True
        VAA = True
        BAA = True
        ABAA = True
        ADM = True
        ODM = True

    ## Crawling data to db ##
        Universe = ['SPY','IWM','QQQ','VGK','EWJ','VWO','VNQ','GSG'
                   ,'GLD','TLT','HYG','LQD','UST','BND','VEA','BIL'
                   ,'TIP','SHV','EFO','EET','EEM','SHY','AGG','SSO'
                   ,'QLD','UWM','UGL','UBT','UJB','IEF','DBC','TNA'
                   ,'VSS','EFA']
        
        df_DB = check_DB_from_drive(Universe, start_day, end_day)

    ## 백테스트 기간 설정 ##
        
        if  CP == True:
            print('# CP   (Original) Back Test #')
            df_CP = CP_MAIN(start_day, end_day, df_DB, Sampling)
            df_CP.to_excel('Report/AA/CP.xlsx')
            df_CP.index = df_CP.index.values.astype('<M8[m]')
            print('# CP   (Leverage) Back Test #')
            df_CP_LV = CP_LV_MAIN(start_day, end_day, df_DB, Sampling)
            df_CP_LV.to_excel('Report/AA/CP_LV.xlsx')
            df_CP_LV.index = df_CP_LV.index.values.astype('<M8[m]')
        else:pass
        if  PP == True:
            print('# PP   (Original) Back Test #')
            df_PP = PP_MAIN(start_day, end_day, df_DB, Sampling)
            df_PP.to_excel('Report/AA/PP.xlsx')
            df_PP.index = df_PP.index.values.astype('<M8[m]')  
            print('# PP   (Leverage) Back Test #')
            df_PP_LV = PP_LV_MAIN(start_day, end_day, df_DB, Sampling)
            df_PP_LV.to_excel('Report/AA/PP_LV.xlsx') 
            df_PP_LV.index = df_PP_LV.index.values.astype('<M8[m]')  
        else:pass        
        if  DAA == True:
            print('# DAA  (Original) Back Test #')
            df_DAA, df_DAA_T = DAA_MAIN(start_day, end_day, df_DB, Sampling)
            df_DAA.to_excel('Report/AA/DAA.xlsx')
            df_DAA.index = df_DAA.index.values.astype('<M8[m]')
            print('# DAA  (Leverage) Back Test #')
            df_DAA_LV, df_DAA_LV_T = DAA_LV_MAIN(start_day, end_day, df_DB, Sampling)
            df_DAA_LV.to_excel('Report/AA/DAA_LV.xlsx')
            df_DAA_LV.index = df_DAA_LV.index.values.astype('<M8[m]')
        else:pass
        if  VAA == True:
            print('# VAA  (Original) Back Test #')
            df_VAA, df_VAA_T = VAA_MAIN(start_day, end_day, df_DB, Sampling)
            df_VAA.to_excel('Report/AA/VAA.xlsx')
            df_VAA.index = df_VAA.index.values.astype('<M8[m]')
            print('# VAA  (Leverage) Back Test #')
            df_VAA_LV, df_VAA_LV_T = VAA_LV_MAIN(start_day, end_day, df_DB, Sampling)
            df_VAA_LV.to_excel('Report/AA/VAA_LV.xlsx')
            df_VAA_LV.index = df_VAA_LV.index.values.astype('<M8[m]')
        else:pass
        if  BAA == True:
            print('# BAA  (Original) Back Test #')
            df_BAA, df_BAA_T = BAA_MAIN(start_day, end_day, df_DB, Sampling)
            df_BAA.to_excel('Report/AA/BAA.xlsx')
            df_BAA.index = df_BAA.index.values.astype('<M8[m]')
            print('# BAA  (Leverage) Back Test #')
            df_BAA_LV, df_BAA_LV_T = BAA_LV_MAIN(start_day, end_day, df_DB, Sampling)
            df_BAA_LV.to_excel('Report/AA/BAA_LV.xlsx')
            df_BAA_LV.index = df_BAA_LV.index.values.astype('<M8[m]')
        else:pass
        if  ABAA == True:
            print('# ABAA (Original) Back Test #')
            df_ABAA, df_ABAA_T = ABAA_MAIN(start_day, end_day, df_DB, Sampling)
            df_ABAA.to_excel('Report/AA/ABAA.xlsx')
            df_ABAA.index = df_ABAA.index.values.astype('<M8[m]')
            print('# ABAA (Leverage) Back Test #')
            df_ABAA_LV, df_ABAA_LV_T = ABAA_LV_MAIN(start_day, end_day, df_DB, Sampling)
            df_ABAA_LV.to_excel('Report/AA/ABAA_LV.xlsx')
            df_ABAA_LV.index = df_ABAA_LV.index.values.astype('<M8[m]')
        else:pass
        if  ADM == True:
            print('# ADM  (Original) Back Test #')
            df_ADM, df_ADM_T = ADM_MAIN(start_day, end_day, df_DB, Sampling)
            df_ADM.to_excel('Report/AA/ADM.xlsx')
            df_ADM.index = df_ADM.index.values.astype('<M8[m]')
            print('# ADM  (Leverage) Back Test #')
            df_ADM_LV, df_ADM_LV_T = ADM_LV_MAIN(start_day, end_day, df_DB, Sampling)
            df_ADM_LV.to_excel('Report/AA/ADM_LV.xlsx')
            df_ADM_LV.index = df_ADM_LV.index.values.astype('<M8[m]')
        else:pass
        if  ODM == True:
            print('# ODM  (Original) Back Test #')
            df_ODM, df_ODM_T = ODM_MAIN(start_day, end_day, df_DB, Sampling)
            df_ODM.to_excel('Report/AA/ODM.xlsx')
            df_ODM.index = df_ODM.index.values.astype('<M8[m]')
            print('# ODM  (Leverage) Back Test #')
            df_ODM_LV, df_ODM_LV_T = ODM_LV_MAIN(start_day, end_day, df_DB, Sampling)
            df_ODM_LV.to_excel('Report/AA/ODM_LV.xlsx')
            df_ODM_LV.index = df_ODM_LV.index.values.astype('<M8[m]')
        else:pass
        
        print('# Merging data frame #')
        if  CP == True:
            df_ALL = df_CP[['CP_BAL','CP_DD']]
            df_ALL_LV = df_CP_LV[['CP_BAL','CP_DD']]
        else:pass
        if  PP == True:
            df_ALL = df_ALL.join(df_PP[['PP_BAL','PP_DD']])
            df_ALL_LV = df_ALL_LV.join(df_PP_LV[['PP_BAL','PP_DD']])
        else:pass
        if  DAA == True:
            df_ALL = df_ALL.join(df_DAA[['DAA_BAL','DAA_DD']])
            df_ALL_LV = df_ALL_LV.join(df_DAA_LV[['DAA_BAL','DAA_DD']])
            df_ALL_T = df_DAA_T
            df_ALL_T = df_ALL_T.join(df_DAA_LV_T)
        else:pass
        if  VAA == True:
            df_ALL = df_ALL.join(df_VAA[['VAA_BAL','VAA_DD']])
            df_ALL_LV = df_ALL_LV.join(df_VAA_LV[['VAA_BAL','VAA_DD']])
            df_ALL_T = df_ALL_T.join(df_VAA_T)
            df_ALL_T = df_ALL_T.join(df_VAA_LV_T)
        else:pass
        if  BAA == True:
            df_ALL = df_ALL.join(df_BAA[['BAA_BAL','BAA_DD']])
            df_ALL_LV = df_ALL_LV.join(df_BAA_LV[['BAA_BAL','BAA_DD']])
            df_ALL_T = df_ALL_T.join(df_BAA_T)
            df_ALL_T = df_ALL_T.join(df_BAA_LV_T)
        else:pass
        if  ABAA == True:
            df_ALL = df_ALL.join(df_ABAA[['ABAA_BAL','ABAA_DD']])
            df_ALL_LV = df_ALL_LV.join(df_ABAA_LV[['ABAA_BAL','ABAA_DD']])
            df_ALL_T = df_ALL_T.join(df_ABAA_T)
            df_ALL_T = df_ALL_T.join(df_ABAA_LV_T)
        else:pass    
        if  ADM == True:
            df_ALL = df_ALL.join(df_ADM[['ADM_BAL','ADM_DD']])
            df_ALL_LV = df_ALL_LV.join(df_ADM_LV[['ADM_BAL','ADM_DD']])
            df_ALL_T = df_ALL_T.join(df_ADM_T)
            df_ALL_T = df_ALL_T.join(df_ADM_LV_T)
        else:pass
        if  ODM == True:
            df_ALL = df_ALL.join(df_ODM[['ODM_BAL','ODM_DD']])
            df_ALL_LV = df_ALL_LV.join(df_ODM_LV[['ODM_BAL','ODM_DD']])
            df_ALL_T = df_ALL_T.join(df_ODM_T)
            df_ALL_T = df_ALL_T.join(df_ODM_LV_T)
        else:pass
        df_ALL.to_excel('Report/AA/df_ALL.xlsx')
        df_ALL_T.to_excel('Report/AA/df_ALL_T.xlsx')
        df_ALL_LV.to_excel('Report/AA/df_ALL_LV.xlsx')

        clear_output(wait=True)
        
        if Plot_Ena == True:
            print('# Plotting.. #')
            mpl.rcParams['axes.unicode_minus'] = False
            plt.rcParams['font.size'] = 15
            plt.rcParams['font.family'] = 'Arial'

            plt.figure(figsize=(20,10))
            if  CP == True: 
                sns.lineplot(data=df_ALL['CP_BAL'] ,label='CP Original')
            else:pass
            if  PP == True: 
                sns.lineplot(data=df_ALL['PP_BAL'] ,label='PP Original')
            else:pass
            if  DAA == True: 
                sns.lineplot(data=df_ALL['DAA_BAL'],label='DAA Original')
            else:pass
            if  VAA == True: 
                sns.lineplot(data=df_ALL['VAA_BAL'],label='VAA Original')
            else:pass
            if  BAA == True: 
                sns.lineplot(data=df_ALL['BAA_BAL'],label='BAA Original')
            else:pass
            if  ABAA == True: 
                sns.lineplot(data=df_ALL['ABAA_BAL'],label='ABAA Original')
            else:pass
            if  ADM == True: 
                sns.lineplot(data=df_ALL['ADM_BAL'],label='ADM Original')
            else:pass

            plt.figure(figsize=(20,10))
            if  CP == True: 
                sns.lineplot(data=df_ALL_LV['CP_BAL'] ,label='CP Leverage')
            else:pass
            if  PP == True: 
                sns.lineplot(data=df_ALL_LV['PP_BAL'] ,label='PP Leverage')
            else:pass
            if  DAA == True: 
                sns.lineplot(data=df_ALL_LV['DAA_BAL'],label='DAA Leverage')
            else:pass
            if  VAA == True: 
                sns.lineplot(data=df_ALL_LV['VAA_BAL'],label='VAA Leverage')
            else:pass
            if  BAA == True: 
                sns.lineplot(data=df_ALL_LV['BAA_BAL'],label='BAA Leverage')
            else:pass
            if  ABAA == True: 
                sns.lineplot(data=df_ALL_LV['ABAA_BAL'],label='ABAA Leverage')
            else:pass
            if  ADM == True: 
                sns.lineplot(data=df_ALL_LV['ADM_BAL'],label='ADM Leverage')
            else:pass
        else:pass
        
        print('# Calculate CAGR & MDD.. #')
        if  CP == True:
            CAGR_CP = qs.stats.cagr(df_ALL['CP_BAL'])
            CAGR_CP_Lv = qs.stats.cagr(df_ALL_LV['CP_BAL'])
            MDD_CP = qs.stats.max_drawdown(df_ALL['CP_BAL'])
            MDD_CP_Lv = qs.stats.max_drawdown(df_ALL_LV['CP_BAL'])
            print('#'*50)
            print('CP   (Ori) - CAGR : {}'.format(round(CAGR_CP*100,2)) + '%' + '   MDD  : {}'.format(round(MDD_CP*100,2)))
            print('CP   (Lev) - CAGR : {}'.format(round(CAGR_CP_Lv*100,2)) + '%' '  MDD  : {}'.format(round(MDD_CP_Lv*100,2)))
        else:pass
        if  PP == True:
            CAGR_PP = qs.stats.cagr(df_ALL['PP_BAL'])
            CAGR_PP_Lv = qs.stats.cagr(df_ALL_LV['PP_BAL'])
            MDD_PP = qs.stats.max_drawdown(df_ALL['PP_BAL'])    
            MDD_PP_Lv = qs.stats.max_drawdown(df_ALL_LV['PP_BAL'])   
            print('#'*50)
            print('PP   (Ori) - CAGR : {}'.format(round(CAGR_PP*100,2)) + '%' + '   MDD  : {}'.format(round(MDD_PP*100,2)) + '%')
            print('PP   (Lev) - CAGR : {}'.format(round(CAGR_PP_Lv*100,2)) + '%' + '   MDD  : {}'.format(round(MDD_PP_Lv*100,2)) + '%')
        else:pass
        if  DAA == True:
            CAGR_DAA = qs.stats.cagr(df_ALL['DAA_BAL'])
            CAGR_DAA_Lv = qs.stats.cagr(df_ALL_LV['DAA_BAL'])
            MDD_DAA = qs.stats.max_drawdown(df_ALL['DAA_BAL'])
            MDD_DAA_Lv = qs.stats.max_drawdown(df_ALL_LV['DAA_BAL'])
            df_ALL_T['DAA']['CAGR'] = round(CAGR_DAA,2)
            df_ALL_T['DAA']['MDD'] = round(MDD_DAA,2)
            df_ALL_T['DAA_LV']['CAGR'] = round(CAGR_DAA_Lv,2)
            df_ALL_T['DAA_LV']['MDD'] = round(MDD_DAA_Lv,2)
            print('#'*50)
            print('DAA  (Ori) - CAGR : {}'.format(round(CAGR_DAA*100,2)) + '%' + '   MDD  : {}'.format(round(MDD_DAA*100,2)) + '%')
            print('DAA  (Lev) - CAGR : {}'.format(round(CAGR_DAA_Lv*100,2)) + '%' + '  MDD  : {}'.format(round(MDD_DAA_Lv*100,2)) + '%')
        else:pass
        if  VAA == True:
            CAGR_VAA = qs.stats.cagr(df_ALL['VAA_BAL'])
            CAGR_VAA_Lv = qs.stats.cagr(df_ALL_LV['VAA_BAL'])
            MDD_VAA = qs.stats.max_drawdown(df_ALL['VAA_BAL'])
            MDD_VAA_Lv = qs.stats.max_drawdown(df_ALL_LV['VAA_BAL'])
            df_ALL_T['VAA']['CAGR'] = round(CAGR_VAA,2)
            df_ALL_T['VAA']['MDD'] = round(MDD_VAA,2)
            df_ALL_T['VAA_LV']['CAGR'] = round(CAGR_VAA_Lv,2)
            df_ALL_T['VAA_LV']['MDD'] = round(MDD_VAA_Lv,2)   
            print('#'*50)
            print('VAA  (Ori) - CAGR : {}'.format(round(CAGR_VAA*100,2)) + '%' + '   MDD  : {}'.format(round(MDD_VAA*100,2)) + '%')
            print('VAA  (Lev) - CAGR : {}'.format(round(CAGR_VAA_Lv*100,2)) + '%' + '  MDD  : {}'.format(round(MDD_VAA_Lv*100,2)) + '%')
        else:pass
        if  BAA == True:
            CAGR_BAA = qs.stats.cagr(df_ALL['BAA_BAL'])
            CAGR_BAA_Lv = qs.stats.cagr(df_ALL_LV['BAA_BAL'])
            MDD_BAA = qs.stats.max_drawdown(df_ALL['BAA_BAL'])
            MDD_BAA_Lv = qs.stats.max_drawdown(df_ALL_LV['BAA_BAL'])
            df_ALL_T['BAA']['CAGR'] = round(CAGR_BAA,2)
            df_ALL_T['BAA']['MDD'] = round(MDD_BAA,2)
            df_ALL_T['BAA_LV']['CAGR'] = round(CAGR_BAA_Lv,2)
            df_ALL_T['BAA_LV']['MDD'] = round(MDD_BAA_Lv,2)  
            print('#'*50)
            print('BAA  (Ori) - CAGR : {}'.format(round(CAGR_BAA*100,2)) + '%' + '   MDD  : {}'.format(round(MDD_BAA*100,2)) + '%')
            print('BAA  (Lev) - CAGR : {}'.format(round(CAGR_BAA_Lv*100,2)) + '%' + '  MDD  : {}'.format(round(MDD_BAA_Lv*100,2)) + '%')
        else:pass
        if  ABAA == True:
            CAGR_ABAA = qs.stats.cagr(df_ALL['ABAA_BAL'])
            CAGR_ABAA_Lv = qs.stats.cagr(df_ALL_LV['ABAA_BAL'])
            MDD_ABAA = qs.stats.max_drawdown(df_ALL['ABAA_BAL'])
            MDD_ABAA_Lv = qs.stats.max_drawdown(df_ALL_LV['ABAA_BAL'])
            df_ALL_T['ABAA']['CAGR'] = round(CAGR_ABAA,2)
            df_ALL_T['ABAA']['MDD'] = round(MDD_ABAA,2)
            df_ALL_T['ABAA_LV']['CAGR'] = round(CAGR_ABAA_Lv,2)
            df_ALL_T['ABAA_LV']['MDD'] = round(MDD_ABAA_Lv,2)   
            print('#'*50)
            print('ABAA (Ori) - CAGR : {}'.format(round(CAGR_ABAA*100,2)) + '%' + '  MDD  : {}'.format(round(MDD_ABAA*100,2)) + '%')
            print('ABAA (Lev) - CAGR : {}'.format(round(CAGR_ABAA_Lv*100,2)) + '%' + '   MDD : {}'.format(round(MDD_ABAA_Lv*100,2)) + '%')
        else:pass
        if  ADM == True:
            CAGR_ADM = qs.stats.cagr(df_ALL['ADM_BAL'])
            CAGR_ADM_Lv = qs.stats.cagr(df_ALL_LV['ADM_BAL'])
            MDD_ADM = qs.stats.max_drawdown(df_ALL['ADM_BAL'])
            MDD_ADM_Lv = qs.stats.max_drawdown(df_ALL_LV['ADM_BAL'])
            df_ALL_T['ADM']['CAGR'] = round(CAGR_ADM,2)
            df_ALL_T['ADM']['MDD'] = round(MDD_ADM,2)
            df_ALL_T['ADM_LV']['CAGR'] = round(CAGR_ADM_Lv,2)
            df_ALL_T['ADM_LV']['MDD'] = round(MDD_ADM_Lv,2)   
            print('#'*50)
            print('ADM  (Ori) - CAGR : {}'.format(round(CAGR_ADM*100,2)) + '%' + '   MDD  : {}'.format(round(MDD_ADM*100,2)) + '%')
            print('ADM  (Lev) - CAGR : {}'.format(round(CAGR_ADM_Lv*100,2)) + '%' + '  MDD  : {}'.format(round(MDD_ADM_Lv*100,2)) + '%')
        else:pass
        if  ODM == True:
            CAGR_ODM = qs.stats.cagr(df_ALL['ODM_BAL'])
            CAGR_ODM_Lv = qs.stats.cagr(df_ALL_LV['ODM_BAL'])
            MDD_ODM = qs.stats.max_drawdown(df_ALL['ODM_BAL'])
            MDD_ODM_Lv = qs.stats.max_drawdown(df_ALL_LV['ODM_BAL'])
            df_ALL_T['ODM']['CAGR'] = round(CAGR_ODM,2)
            df_ALL_T['ODM']['MDD'] = round(MDD_ODM,2)
            df_ALL_T['ODM_LV']['CAGR'] = round(CAGR_ODM_Lv,2)
            df_ALL_T['ODM_LV']['MDD'] = round(MDD_ODM_Lv,2)  
            print('#'*50)
            print('ODM  (Ori) - CAGR : {}'.format(round(CAGR_ODM*100,2)) + '%' + '   MDD  : {}'.format(round(MDD_ODM*100,2)) + '%')
            print('ODM  (Lev) - CAGR : {}'.format(round(CAGR_ODM_Lv*100,2)) + '%' + '  MDD  : {}'.format(round(MDD_ODM_Lv*100,2)) + '%')
        else:pass
        
        return df_ALL, df_ALL_LV, df_ALL_T

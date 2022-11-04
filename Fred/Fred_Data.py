import pandas_datareader as pdr
import pandas as pd
import numpy as np
import FinanceDataReader as fdr

from datetime import datetime, timedelta

def get_datareader_Fred_data(start_day, end_day):
    
    # 2020년~현재의 나스닥지수(NASDAQCOM)와 주간 실업수당 청구 건수(ICSA) 추이  
    # M1 / M2 통화량 #
    # M1 (협의통화): 현금통화 + 요구불예금.수시입출식 저축성예금 - 동 금융상품의 예금취급기관 간 상호거래분 #
    # M2 (광의통화): M1 + 기간물 정기예금,적금 및 부금 + 시장형금융상품(CD,RP,표지어음) + 실적 배당형금융상품(금전신탁,수익증권 등) + 금융채 + 기타(투신증권저축, 종금사 발행어음) - 동 금융상품 중 장기(만기 2년이상) 상품 - 동 금융상품의 예금취급기관 간 상호거래분
    # BAMLH0A0HYM2 : 하이일드 채권 수익률 - 미국 국채 수익률 #
    
    df_ALL = fdr.DataReader(['ICSA','M1','M2','BAMLH0A0HYM2','DFF','NASDAQCOM','SP500'], start=start_day, end=end_day, data_source='fred')
    
    #df_M2   = fdr.DataReader(['NASDAQCOM', 'M2'], start=start_day, end=end_day, data_source='fred')
    #df_SPRD = fdr.DataReader(['NASDAQCOM', 'BAMLH0A0HYM2'], start=start_day, end=end_day, data_source='fred')
    
    #df_INDEX = fdr.DataReader(['NASDAQCOM','SP500'], start=start_day, end=end_day, data_source='fred')
    #df_INTEREST = fdr.DataReader(['BAMLH0A0HYM2','DFF'], start=start_day, end=end_day, data_source='fred')
    #df_QT = fdr.DataReader(['M1','M2'], start=start_day, end=end_day, data_source='fred')
    
    P_col_list = [col+'_P' for col in df_ALL.columns]
    df_ALL[P_col_list] = df_ALL.pct_change()
    df_ALL[P_col_list] = df_ALL[P_col_list]*100
    

    mva_col_list = [col+'_MVA' for col in df_ALL.columns]
    df_ALL[mva_col_list] = df_ALL.rolling(window=365,min_periods=1).mean()

    for i in range(len(df_ALL)):
        
        
        df_ALL.loc[df_ALL.index[i],'M1_L_P_MVA'] = np.log(df_ALL['M1_P_MVA'].iloc[i]+1)
        df_ALL.loc[df_ALL.index[i],'M1_L_P_MVA'] = np.log(df_ALL['M1_P_MVA'].iloc[i]+1)
        
        df_ALL.loc[df_ALL.index[i],'M1_L_MVA'] = np.log(df_ALL['M1_MVA'].iloc[i]+1)
        df_ALL.loc[df_ALL.index[i],'M2_L_MVA'] = np.log(df_ALL['M2_MVA'].iloc[i]+1)
        
        df_ALL.loc[df_ALL.index[i],'NASDAQCOM_L'] = np.log(df_ALL['NASDAQCOM'].iloc[i]+1)
        df_ALL.loc[df_ALL.index[i],'SP500_L'] = np.log(df_ALL['SP500'].iloc[i]+1)
    
    df_ALL = df_ALL[start_day:end_day]
    
    return df_ALL

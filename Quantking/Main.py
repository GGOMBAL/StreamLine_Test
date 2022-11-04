import quantstats as qs
import time

from Quantking.Set_Universe import *
from Quantking.Strategy_Mix import *
from BenchMark.Benchmark import *

class QK:
    
    def Quant_Main():

        #Strategy_Mix()

    ## 백테스트 기간 설정 ##
        #start_day = datetime(2012,4,1)
        #end_day = datetime.now()

    ## Monthly rebalancing yes or not ##
        df_QT_1Y = Sel_Quant_Universe_1Y(True,1,3)   
        df_QT_1Y = df_QT_1Y.rename({'ASSET_BAL': 'QT1_BAL','ASSET_P': 'QT1_P'}, axis=1)

        df_QT_4Q = Sel_Quant_Universe_4Q(True,1,3)
        #df_QT_4Q = df_QT_4Q.rename({'ASSET_BAL': 'QT2_BAL','ASSET_P': 'QT2_P'}, axis=1)
        #print(df_QT_4Q['QT2_BAL'].tail())

        #Strategy_Mix(df_QT_1Y['QT1_BAL','QT1_P'], df_QT_4Q['QT2_BAL','QT2_P'])

    ## Export excel file ##
        df_QT_1Y.to_excel('Report/QK/1Y.xlsx')
        df_QT_4Q.to_excel('Report/QK/4Q.xlsx')


        return df_QT_1Y, df_QT_4Q
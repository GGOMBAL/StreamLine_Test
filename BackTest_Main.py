#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[ ]:
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from datetime import datetime, timedelta
from DB.db_helper import *
#from MakeGUI.Gui_Main import *
from PyQt5  import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QWidget

import matplotlib.pyplot as plt
import quantstats as qs
import seaborn as sns

from AssetAllocation.AA_Main import AA
from BenchMark.Benchmark import BM
from Quantking.Main import QK
from Market_Timing.MT_Main import MT
from Fred.Fred_Main import FRED

## 백테스트 기간 설정 ##

#global start_day, end_day
global M_GUI, M_BM, M_AA, M_QK, M_MT, M_FRED

M_GUI = False
M_BM  = False
M_AA  = True
M_QK  = False
M_MT  = False
M_FRED = False

#now = datetime.now().strftime("%Y%m%d")
start_day = datetime(2012,1,1)
end_day = datetime.today()
        
if  M_GUI == True:
    print('# GUI Main #')
    #app = QtWidgets.QApplication(sys.argv)
    #MainWindow = QtWidgets.QMainWindow()
    #ui = MyWindow()
    #
    #try:
    #    ui.setupUi(MainWindow)        
    #    MainWindow.show()
    #except Exception as e:
    #    ui.Eem_ExceptionProcedure(e)
    #    os.system('pause')
    #    
    #sys.exit(app.exec_())
else:pass
if  M_FRED == True:
    print('# Gathering Fred info.. #')
    df_FRED = FRED.Fred_Main(start_day,end_day)
    insert_df_to_db('FRED_Data', 'FRED', df_FRED, option="replace")    
else:pass

if  M_AA == True:
    print('# Asset Allocation Back Test.. #')
    df_AA, df_AA_LV, df_ALL_T = AA.AA_Main(start_day,end_day)
    insert_df_to_db('AA_Data', 'AA', df_AA, option="replace")
    insert_df_to_db('AA_Lev_Data', 'AA_Lev', df_AA_LV, option="replace")
    insert_df_to_db('AA_Today', 'AA_T', df_ALL_T, option="replace")
else:pass

if  M_BM == True:
    print('# Call BenchMark.. #')
    df_BM = BM.get_BenchMark(start_day,end_day)
    insert_df_to_db('BM_Data', 'BM', df_AA, option="replace")
else:pass

if  M_QK == True:
    print('# Quantking Back Test.. #')
    df_QT_1Y, df_QT_4Q = QK.Quant_Main()
    #insert_df_to_db('QK_Data', 'QK', df_AA, option="replace")
else:pass

if  M_MT == True:
    print('# Market Timing BackTest.. #')
    df_MT = MT.Market_Timing_backtest(df_QT_1Y, df_FRED)
else:pass

print('# Generate Report.. #')

#if  M_QK == True:
    #qs.reports.html(df_QT_1Y['ASSET_BAL'], mode='full', title='Quant 1Y', download_filename='Quantking-1Y.html')    
    #qs.reports.html(df_QT_4Q['ASSET_BAL'], mode='full', title='Quant 4Q', download_filename='Quantking-4Q.html')
#else:pass

if  M_AA == True:
    qs.reports.html(df_AA['BAA_BAL'], mode='full', title='BAA(ORI)', download_filename='BAA.html')    
else:pass

#if  M_MT == True:
    #qs.reports.html(df_MT['TOTAL_BAL'],'^KS11', mode='full', title='MT+Quant', download_filename='MT+Quant.html')    
    #qs.reports.html(df_MT['ASSET_BAL'],'^KS11', mode='full', title='Quant', download_filename='Quant.html')
#else:pass

print('# Done #\n')




 # %%


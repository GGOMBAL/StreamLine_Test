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
from PyQt5  import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QWidget

import matplotlib.pyplot as plt
import quantstats as qs
import seaborn as sns

from AssetAllocation.AA_Main import AA
from BenchMark.Benchmark import BM
from Quantking.Main import QK
from Fred.Fred_Main import FRED

## 백테스트 기간 설정 ##

#global start_day, end_day
global M_BM, M_AA, M_QK, M_FRED

M_BM  = False
M_AA  = True
M_QK  = False
M_FRED = False
       
#now = datetime.now().strftime("%Y%m%d")
start_day = datetime(2012,1,1)
end_day = datetime.today()
        
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

print('# Done #\n')




 # %%


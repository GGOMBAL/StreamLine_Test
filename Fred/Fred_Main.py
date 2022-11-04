import pandas_datareader as pdr
import pandas as pd
import numpy as np
import FinanceDataReader as fdr
from Fred.Fred_Data import *

from datetime import datetime, timedelta

class FRED:
    
    def Fred_Main(start_day, end_day):
    
        #df_ALL = check_DB_from_drive(Universe, start_day, end_day)
        
        df_ALL = get_datareader_Fred_data(start_day, end_day)
    
        return df_ALL
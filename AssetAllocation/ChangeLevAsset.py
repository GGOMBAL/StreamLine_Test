import pandas as pd
import numpy as np

def ChangeRevAsset(AA_List):
    
    return 

def ChangeKorAsset(df_DB):
    
    global New_Val_List
    
    Universe = ['SPY','IWM','QQQ','VGK','EWJ','VWO','VNQ','GSG'
               ,'GLD','TLT','HYG','LQD','UST','BND','VEA','BIL'
               ,'TIP','SHV','EFO','EET','EEM','SHY','AGG','SSO'
               ,'QLD','UWM','UGL','UBT','UJB','IEF','DBC','TNA'
               ,'VSS','EFA']
    
    mydic =  {'SPY':'379800','QQQ':'379810','IWM':'280930','GLD':'132030'
             ,'TLT':'304660','HYG':'182490','VGK':'195930','EWJ':'241180'
             ,'VNQ':'181480','EEM':'291890','GSG':'218420','SHV':'214980'
             ,'IEF':'114460','HYG':'136340','EFA':'251350','AGG':'273130'
             ,'LQD':'332620','SHY':'261240','DBC':'261220','BIL':'329750'}
       
    for i in range(len(df_DB.columns)):
        keys = df_DB[df_DB.columns[i]]['ASSET']
                       
        if str(keys).find(',')!=-1:
            strings = keys.split(',')
            New_Val_List = list()
            New_Val = '' 
            
            for j in range(len(strings)):
                                
                if strings[j] in mydic:
                    New_Val_List.append(str(mydic[strings[j]]))
                    New_Val = ', '.join(New_Val_List)
                    df_DB[df_DB.columns[i]]['ASSET'] = New_Val
                else:pass           
        else: 
            Rep_Asset = mydic[df_DB[df_DB.columns[i]]['ASSET']]
            df_DB[df_DB.columns[i]]['ASSET'] = Rep_Asset
            
    return df_DB


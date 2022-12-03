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
    
    mydic =  {'SPY':'379800','IWM':'280930','QQQ':'379810','VGK':'195930','EWJ':'241180','VWO':'195980','VNQ':'181480','GSG':'218420'
             ,'GLD':'132030','TLT':'304660','HYG':'182490','LQD':'332620','UST':'xxxxxx','BND':'xxxxxx','VEA':'xxxxxx','BIL':'329750'
             ,'TIP':'xxxxxx','SHV':'214980','EFO':'214980','EET':'214980','EEM':'291890','SHY':'261240','AGG':'273130','SSO':'xxxxxx'
             ,'QLD':'xxxxxx','UWM':'xxxxxx','UGL':'xxxxxx','UBT':'xxxxxx','UJB':'xxxxxx','IEF':'114460','DBC':'261220','TNA':'xxxxxx'
             ,'VSS':'xxxxxx','EFA':'251350'}
       
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


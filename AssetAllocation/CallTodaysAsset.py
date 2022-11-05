import pandas as pd
import numpy as np

def Call_AA_Today_2(df_ALL,AA_Name,AA_T_List):

    AssetList_Temp = []
    Today_AssetList_sort = []
    AssetList = []
    
    AssetList_Temp = list(df_ALL[AA_T_List].iloc[-1])    
    df_AA_T = pd.DataFrame(columns=[AA_Name],index=['Position','ASSET','CASH','CAGR','MDD'])
    
    for i in range(len(AssetList_Temp)):
        temp_asset = AssetList_Temp[i]
        
        if temp_asset not in Today_AssetList_sort:
           Today_AssetList_sort.append(temp_asset)        

    if AssetList_Temp[-1] == 'Deffensive':
        Today_AssetList_sort.remove('Deffensive')                
    else:
        Today_AssetList_sort.remove('Offensive')       

    Assetstr = ''
    Assetstr = ','.join(Today_AssetList_sort)
    
    df_AA_T.loc['Position',AA_Name] = AssetList_Temp[-1]
    df_AA_T.loc['ASSET',AA_Name] = Assetstr
    df_AA_T.loc['CASH',AA_Name] = 0             

    return df_AA_T

def Call_AA_Today(df_ALL,Offensive,Defensive,AA_Name,AA_T_List):
    
    AssetList_Temp = []
    Today_AssetList_sort = []
    AssetList = []
    
    AssetList_Temp = list(df_ALL[AA_T_List].iloc[-1])
    
    df_AA_T = pd.DataFrame(columns=[AA_Name],index=['Position','ASSET','CASH','CAGR','MDD'])
        
    if AssetList_Temp[-1] == 'Deffensive':
        CASH_Cnt = AssetList_Temp.count('CASH')
    else:
        CASH_Cnt = 0
        
    for i in range(len(AssetList_Temp)):
        temp_asset = AssetList_Temp[i]
        
        if temp_asset not in Today_AssetList_sort:
           Today_AssetList_sort.append(temp_asset)
    
    if AssetList_Temp[-1] == 'Deffensive':
        Today_AssetList_sort.remove('Deffensive')
        
        if CASH_Cnt>0:
            Today_AssetList_sort.remove('CASH')
        
        
        for j in range(len(Today_AssetList_sort)):
            AssetList.append(Defensive[int(Today_AssetList_sort[j][-1])])
    else:
        Today_AssetList_sort.remove('Offensive')
        
        for j in range(len(Today_AssetList_sort)):
            AssetList.append(Offensive[int(Today_AssetList_sort[j][-1])])

    Assetstr = ''
    Assetstr = ','.join(AssetList)
    
    df_AA_T.loc['Position',AA_Name] = AssetList_Temp[-1]
    df_AA_T.loc['ASSET',AA_Name] = Assetstr
    df_AA_T.loc['CASH',AA_Name] = round((float(CASH_Cnt) / float(len(AssetList_Temp)-1)) *100,1)

    return df_AA_T
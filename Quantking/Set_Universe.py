from Quantking.Rebalancing import *

def Sel_Quant_Universe_1Y(Rebalancing,Fee_M,Fee_Q):

    End_of_Q_Reval_Fee = Fee_Q
    
    df_Ticker = pd.read_excel(r'InExcel\QuantKing_Ticker_1Y.xlsx', sheet_name='Sheet1',header= 0,index_col='Date',dtype=str,na_values ='NaN')
    
    Universe2012_1Y = [str(x) for x in list(df_Ticker.loc[2012])]
    Universe2013_1Y = [str(x) for x in list(df_Ticker.loc[2013])]
    Universe2014_1Y = [str(x) for x in list(df_Ticker.loc[2014])]
    Universe2015_1Y = [str(x) for x in list(df_Ticker.loc[2015])]
    Universe2016_1Y = [str(x) for x in list(df_Ticker.loc[2016])]
    Universe2017_1Y = [str(x) for x in list(df_Ticker.loc[2017])]
    Universe2018_1Y = [str(x) for x in list(df_Ticker.loc[2018])]
    Universe2019_1Y = [str(x) for x in list(df_Ticker.loc[2019])]
    Universe2020_1Y = [str(x) for x in list(df_Ticker.loc[2020])]
    Universe2021_1Y = [str(x) for x in list(df_Ticker.loc[2021])]
    Universe2022_1Y = [str(x) for x in list(df_Ticker.loc[2022])]
    
    Universe2012_1Y = [x for x in Universe2012_1Y if x != 'nan']
    Universe2013_1Y = [x for x in Universe2013_1Y if x != 'nan']
    Universe2014_1Y = [x for x in Universe2014_1Y if x != 'nan']
    Universe2015_1Y = [x for x in Universe2015_1Y if x != 'nan']
    Universe2016_1Y = [x for x in Universe2016_1Y if x != 'nan']
    Universe2017_1Y = [x for x in Universe2017_1Y if x != 'nan']
    Universe2018_1Y = [x for x in Universe2018_1Y if x != 'nan']
    Universe2019_1Y = [x for x in Universe2019_1Y if x != 'nan']
    Universe2020_1Y = [x for x in Universe2020_1Y if x != 'nan']
    Universe2021_1Y = [x for x in Universe2021_1Y if x != 'nan']
    Universe2022_1Y = [x for x in Universe2022_1Y if x != 'nan']

    Balance_Init = 100

    df_ALL_2012, Balance = Asset_Rebalancing(Universe2012_1Y,Balance_Init,datetime(2012,4,1), datetime(2013,4,1),Rebalancing,Fee_M)
    df_ALL_2013, Balance = Asset_Rebalancing(Universe2013_1Y,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2013,4,2), datetime(2014,4,1),Rebalancing,Fee_M)
    df_ALL_2014, Balance = Asset_Rebalancing(Universe2014_1Y,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2014,4,2), datetime(2015,4,1),Rebalancing,Fee_M)
    df_ALL_2015, Balance = Asset_Rebalancing(Universe2015_1Y,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2015,4,2), datetime(2016,4,1),Rebalancing,Fee_M)
    df_ALL_2016, Balance = Asset_Rebalancing(Universe2016_1Y,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2016,4,2), datetime(2017,4,1),Rebalancing,Fee_M)
    df_ALL_2017, Balance = Asset_Rebalancing(Universe2017_1Y,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2017,4,2), datetime(2018,4,1),Rebalancing,Fee_M)
    df_ALL_2018, Balance = Asset_Rebalancing(Universe2018_1Y,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2018,4,2), datetime(2019,4,1),Rebalancing,Fee_M)
    df_ALL_2019, Balance = Asset_Rebalancing(Universe2019_1Y,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2019,4,2), datetime(2020,4,1),Rebalancing,Fee_M)
    df_ALL_2020, Balance = Asset_Rebalancing(Universe2020_1Y,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2020,4,2), datetime(2021,4,1),Rebalancing,Fee_M)
    df_ALL_2021, Balance = Asset_Rebalancing(Universe2021_1Y,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2021,4,2), datetime(2022,4,1),Rebalancing,Fee_M)
    df_ALL_2022, Balance = Asset_Rebalancing(Universe2022_1Y,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2022,4,2), datetime(2022,8,31),Rebalancing,Fee_M)
    
    df_ALL = pd.concat([df_ALL_2012,df_ALL_2013])
    df_ALL = pd.concat([df_ALL,df_ALL_2014])
    df_ALL = pd.concat([df_ALL,df_ALL_2015])
    df_ALL = pd.concat([df_ALL,df_ALL_2016])
    df_ALL = pd.concat([df_ALL,df_ALL_2017])
    df_ALL = pd.concat([df_ALL,df_ALL_2018])
    df_ALL = pd.concat([df_ALL,df_ALL_2019])
    df_ALL = pd.concat([df_ALL,df_ALL_2020])
    df_ALL = pd.concat([df_ALL,df_ALL_2021])
    df_ALL = pd.concat([df_ALL,df_ALL_2022])

    df_ALL = df_ALL.fillna(0)
    
    return df_ALL


def Sel_Quant_Universe_4Q(Rebalancing,Fee_M,Fee_Q):
    
# 분기 리벨런싱 슬리피지
    End_of_Q_Reval_Fee = Fee_Q

    df_Ticker = pd.read_excel(r'InExcel\QuantKing_Ticker_4Q.xlsx', sheet_name='Sheet1',header= 0,index_col='Date',dtype=str,na_values ='NaN')
        
    Universe2012_1Q = [str(x) for x in list(df_Ticker.loc['2012_1Q'])]
    Universe2012_2Q = [str(x) for x in list(df_Ticker.loc['2012_2Q'])]
    Universe2012_3Q = [str(x) for x in list(df_Ticker.loc['2012_3Q'])]
    Universe2012_4Q = [str(x) for x in list(df_Ticker.loc['2012_4Q'])]
    
    Universe2012_1Q = [x for x in Universe2012_1Q if x != 'nan']
    Universe2012_2Q = [x for x in Universe2012_2Q if x != 'nan']
    Universe2012_3Q = [x for x in Universe2012_3Q if x != 'nan']
    Universe2012_4Q = [x for x in Universe2012_4Q if x != 'nan']
    
    Universe2013_1Q = [str(x) for x in list(df_Ticker.loc['2013_1Q'])]
    Universe2013_2Q = [str(x) for x in list(df_Ticker.loc['2013_2Q'])]
    Universe2013_3Q = [str(x) for x in list(df_Ticker.loc['2013_3Q'])]
    Universe2013_4Q = [str(x) for x in list(df_Ticker.loc['2013_4Q'])]

    Universe2013_1Q = [x for x in Universe2013_1Q if x != 'nan']
    Universe2013_2Q = [x for x in Universe2013_2Q if x != 'nan']
    Universe2013_3Q = [x for x in Universe2013_3Q if x != 'nan']
    Universe2013_4Q = [x for x in Universe2013_4Q if x != 'nan']
        
    Universe2014_1Q = [str(x) for x in list(df_Ticker.loc['2014_1Q'])]
    Universe2014_2Q = [str(x) for x in list(df_Ticker.loc['2014_2Q'])]
    Universe2014_3Q = [str(x) for x in list(df_Ticker.loc['2014_3Q'])]
    Universe2014_4Q = [str(x) for x in list(df_Ticker.loc['2014_4Q'])]

    Universe2014_1Q = [x for x in Universe2014_1Q if x != 'nan']
    Universe2014_2Q = [x for x in Universe2014_2Q if x != 'nan']
    Universe2014_3Q = [x for x in Universe2014_3Q if x != 'nan']
    Universe2014_4Q = [x for x in Universe2014_4Q if x != 'nan']
    
    Universe2015_1Q = [str(x) for x in list(df_Ticker.loc['2015_1Q'])]
    Universe2015_2Q = [str(x) for x in list(df_Ticker.loc['2015_2Q'])]
    Universe2015_3Q = [str(x) for x in list(df_Ticker.loc['2015_3Q'])]
    Universe2015_4Q = [str(x) for x in list(df_Ticker.loc['2015_4Q'])]
    
    Universe2015_1Q = [x for x in Universe2015_1Q if x != 'nan']
    Universe2015_2Q = [x for x in Universe2015_2Q if x != 'nan']
    Universe2015_3Q = [x for x in Universe2015_3Q if x != 'nan']
    Universe2015_4Q = [x for x in Universe2015_4Q if x != 'nan']
    
    Universe2016_1Q = [str(x) for x in list(df_Ticker.loc['2016_1Q'])]
    Universe2016_2Q = [str(x) for x in list(df_Ticker.loc['2016_2Q'])]
    Universe2016_3Q = [str(x) for x in list(df_Ticker.loc['2016_3Q'])]
    Universe2016_4Q = [str(x) for x in list(df_Ticker.loc['2016_4Q'])]
    
    Universe2016_1Q = [x for x in Universe2016_1Q if x != 'nan']
    Universe2016_2Q = [x for x in Universe2016_2Q if x != 'nan']
    Universe2016_3Q = [x for x in Universe2016_3Q if x != 'nan']
    Universe2016_4Q = [x for x in Universe2016_4Q if x != 'nan']
        
    Universe2017_1Q = [str(x) for x in list(df_Ticker.loc['2017_1Q'])]
    Universe2017_2Q = [str(x) for x in list(df_Ticker.loc['2017_2Q'])]
    Universe2017_3Q = [str(x) for x in list(df_Ticker.loc['2017_3Q'])]
    Universe2017_4Q = [str(x) for x in list(df_Ticker.loc['2017_4Q'])]
    
    Universe2017_1Q = [x for x in Universe2017_1Q if x != 'nan']
    Universe2017_2Q = [x for x in Universe2017_2Q if x != 'nan']
    Universe2017_3Q = [x for x in Universe2017_3Q if x != 'nan']
    Universe2017_4Q = [x for x in Universe2017_4Q if x != 'nan']
    
    Universe2018_1Q = [str(x) for x in list(df_Ticker.loc['2018_1Q'])]
    Universe2018_2Q = [str(x) for x in list(df_Ticker.loc['2018_2Q'])]
    Universe2018_3Q = [str(x) for x in list(df_Ticker.loc['2018_3Q'])]
    Universe2018_4Q = [str(x) for x in list(df_Ticker.loc['2018_4Q'])]
    
    Universe2018_1Q = [x for x in Universe2018_1Q if x != 'nan']
    Universe2018_2Q = [x for x in Universe2018_2Q if x != 'nan']
    Universe2018_3Q = [x for x in Universe2018_3Q if x != 'nan']
    Universe2018_4Q = [x for x in Universe2018_4Q if x != 'nan']
    
    Universe2019_1Q = [str(x) for x in list(df_Ticker.loc['2019_1Q'])]
    Universe2019_2Q = [str(x) for x in list(df_Ticker.loc['2019_2Q'])]
    Universe2019_3Q = [str(x) for x in list(df_Ticker.loc['2019_3Q'])]
    Universe2019_4Q = [str(x) for x in list(df_Ticker.loc['2019_4Q'])]
    
    Universe2019_1Q = [x for x in Universe2019_1Q if x != 'nan']
    Universe2019_2Q = [x for x in Universe2019_2Q if x != 'nan']
    Universe2019_3Q = [x for x in Universe2019_3Q if x != 'nan']
    Universe2019_4Q = [x for x in Universe2019_4Q if x != 'nan']
    
    Universe2020_1Q = [str(x) for x in list(df_Ticker.loc['2020_1Q'])]
    Universe2020_2Q = [str(x) for x in list(df_Ticker.loc['2020_2Q'])]
    Universe2020_3Q = [str(x) for x in list(df_Ticker.loc['2020_3Q'])]
    Universe2020_4Q = [str(x) for x in list(df_Ticker.loc['2020_4Q'])]
    
    Universe2020_1Q = [x for x in Universe2020_1Q if x != 'nan']
    Universe2020_2Q = [x for x in Universe2020_2Q if x != 'nan']
    Universe2020_3Q = [x for x in Universe2020_3Q if x != 'nan']
    Universe2020_4Q = [x for x in Universe2020_4Q if x != 'nan']
    
    Universe2021_1Q = [str(x) for x in list(df_Ticker.loc['2021_1Q'])]
    Universe2021_2Q = [str(x) for x in list(df_Ticker.loc['2021_2Q'])]
    Universe2021_3Q = [str(x) for x in list(df_Ticker.loc['2021_3Q'])]
    Universe2021_4Q = [str(x) for x in list(df_Ticker.loc['2021_4Q'])]
    
    Universe2021_1Q = [x for x in Universe2021_1Q if x != 'nan']
    Universe2021_2Q = [x for x in Universe2021_2Q if x != 'nan']
    Universe2021_3Q = [x for x in Universe2021_3Q if x != 'nan']
    Universe2021_4Q = [x for x in Universe2021_4Q if x != 'nan']
    
    Universe2022_1Q = [str(x) for x in list(df_Ticker.loc['2022_1Q'])]
    Universe2022_2Q = [str(x) for x in list(df_Ticker.loc['2022_2Q'])]
    Universe2022_3Q = [str(x) for x in list(df_Ticker.loc['2022_3Q'])]
    #Universe2022_4Q = [str(x) for x in list(df_Ticker.loc['2022_4Q'])] 
    
    Universe2022_1Q = [x for x in Universe2022_1Q if x != 'nan']
    Universe2022_2Q = [x for x in Universe2022_2Q if x != 'nan']
    Universe2022_3Q = [x for x in Universe2022_3Q if x != 'nan']
    
    
    Balance_Init = 100

    df_ALL_2012_1Q, Balance = Asset_Rebalancing(Universe2012_1Q,Balance_Init,datetime(2012,4,2), datetime(2012,5,18),Rebalancing,Fee_M)
    df_ALL_2012_2Q, Balance = Asset_Rebalancing(Universe2012_2Q,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2012,5,19), datetime(2012,8,18),Rebalancing,Fee_M)
    df_ALL_2012_3Q, Balance = Asset_Rebalancing(Universe2012_3Q,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2012,8,19), datetime(2012,11,18),Rebalancing,Fee_M)
    df_ALL_2012_4Q, Balance = Asset_Rebalancing(Universe2012_4Q,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2012,11,19),datetime(2013,4,1),Rebalancing,Fee_M)
    
    df_ALL_2013_1Q, Balance = Asset_Rebalancing(Universe2013_1Q,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2013,4,2),  datetime(2013,5,18), Rebalancing,Fee_M)
    df_ALL_2013_2Q, Balance = Asset_Rebalancing(Universe2013_2Q,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2013,5,19), datetime(2013,8,18), Rebalancing,Fee_M)
    df_ALL_2013_3Q, Balance = Asset_Rebalancing(Universe2013_3Q,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2013,8,19), datetime(2013,11,18),Rebalancing,Fee_M)
    df_ALL_2013_4Q, Balance = Asset_Rebalancing(Universe2013_4Q,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2013,11,19),datetime(2014,4,1),  Rebalancing,Fee_M)

    df_ALL_2014_1Q, Balance = Asset_Rebalancing(Universe2014_1Q,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2014,4,2),  datetime(2014,5,18), Rebalancing,Fee_M)
    df_ALL_2014_2Q, Balance = Asset_Rebalancing(Universe2014_2Q,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2014,5,19), datetime(2014,8,18), Rebalancing,Fee_M)
    df_ALL_2014_3Q, Balance = Asset_Rebalancing(Universe2014_3Q,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2014,8,19), datetime(2014,11,18),Rebalancing,Fee_M)
    df_ALL_2014_4Q, Balance = Asset_Rebalancing(Universe2014_4Q,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2014,11,19),datetime(2015,4,1),  Rebalancing,Fee_M)

    df_ALL_2015_1Q, Balance = Asset_Rebalancing(Universe2015_1Q,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2015,4,2),  datetime(2015,5,18), Rebalancing,Fee_M)
    df_ALL_2015_2Q, Balance = Asset_Rebalancing(Universe2015_2Q,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2015,5,19), datetime(2015,8,18), Rebalancing,Fee_M)
    df_ALL_2015_3Q, Balance = Asset_Rebalancing(Universe2015_3Q,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2015,8,19), datetime(2015,11,18),Rebalancing,Fee_M)
    df_ALL_2015_4Q, Balance = Asset_Rebalancing(Universe2015_4Q,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2015,11,19),datetime(2016,4,1),  Rebalancing,Fee_M)

    df_ALL_2016_1Q, Balance = Asset_Rebalancing(Universe2016_1Q,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2016,4,2),  datetime(2016,5,18), Rebalancing,Fee_M)
    df_ALL_2016_2Q, Balance = Asset_Rebalancing(Universe2016_2Q,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2016,5,19), datetime(2016,8,18), Rebalancing,Fee_M)
    df_ALL_2016_3Q, Balance = Asset_Rebalancing(Universe2016_3Q,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2016,8,19), datetime(2016,11,18),Rebalancing,Fee_M)
    df_ALL_2016_4Q, Balance = Asset_Rebalancing(Universe2016_4Q,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2016,11,19),datetime(2017,4,1),  Rebalancing,Fee_M)

    df_ALL_2017_1Q, Balance = Asset_Rebalancing(Universe2017_1Q,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2017,4,2),  datetime(2017,5,18), Rebalancing,Fee_M)
    df_ALL_2017_2Q, Balance = Asset_Rebalancing(Universe2017_2Q,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2017,5,19), datetime(2017,8,18), Rebalancing,Fee_M)
    df_ALL_2017_3Q, Balance = Asset_Rebalancing(Universe2017_3Q,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2017,8,19), datetime(2017,11,18),Rebalancing,Fee_M)
    df_ALL_2017_4Q, Balance = Asset_Rebalancing(Universe2017_4Q,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2017,11,19),datetime(2018,4,1),  Rebalancing,Fee_M)
    
    df_ALL_2018_1Q, Balance = Asset_Rebalancing(Universe2018_1Q,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2018,4,2),  datetime(2018,5,18), Rebalancing,Fee_M)
    df_ALL_2018_2Q, Balance = Asset_Rebalancing(Universe2018_2Q,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2018,5,19), datetime(2018,8,18), Rebalancing,Fee_M)
    df_ALL_2018_3Q, Balance = Asset_Rebalancing(Universe2018_3Q,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2018,8,19), datetime(2018,11,18),Rebalancing,Fee_M)
    df_ALL_2018_4Q, Balance = Asset_Rebalancing(Universe2018_4Q,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2018,11,19),datetime(2019,4,1),  Rebalancing,Fee_M)
    
    df_ALL_2019_1Q, Balance = Asset_Rebalancing(Universe2019_1Q,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2019,4,2),  datetime(2019,5,18), Rebalancing,Fee_M)
    df_ALL_2019_2Q, Balance = Asset_Rebalancing(Universe2019_2Q,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2019,5,19), datetime(2019,8,18), Rebalancing,Fee_M)
    df_ALL_2019_3Q, Balance = Asset_Rebalancing(Universe2019_3Q,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2019,8,19), datetime(2019,11,18),Rebalancing,Fee_M)
    df_ALL_2019_4Q, Balance = Asset_Rebalancing(Universe2019_4Q,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2019,11,19),datetime(2020,4,1),  Rebalancing,Fee_M)
    
    df_ALL_2020_1Q, Balance = Asset_Rebalancing(Universe2020_1Q,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2020,4,2),  datetime(2020,5,18), Rebalancing,Fee_M)
    df_ALL_2020_2Q, Balance = Asset_Rebalancing(Universe2020_2Q,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2020,5,19), datetime(2020,8,18), Rebalancing,Fee_M)
    df_ALL_2020_3Q, Balance = Asset_Rebalancing(Universe2020_3Q,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2020,8,19), datetime(2020,11,18),Rebalancing,Fee_M)
    df_ALL_2020_4Q, Balance = Asset_Rebalancing(Universe2020_4Q,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2020,11,19),datetime(2021,4,1),  Rebalancing,Fee_M)
    
    df_ALL_2021_1Q, Balance = Asset_Rebalancing(Universe2021_1Q,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2021,4,2),  datetime(2021,5,18), Rebalancing,Fee_M)
    df_ALL_2021_2Q, Balance = Asset_Rebalancing(Universe2021_2Q,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2021,5,19), datetime(2021,8,18), Rebalancing,Fee_M)
    df_ALL_2021_3Q, Balance = Asset_Rebalancing(Universe2021_3Q,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2021,8,19), datetime(2021,11,18),Rebalancing,Fee_M)
    df_ALL_2021_4Q, Balance = Asset_Rebalancing(Universe2021_4Q,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2021,11,19),datetime(2022,4,1),  Rebalancing,Fee_M)

    df_ALL_2022_1Q, Balance = Asset_Rebalancing(Universe2022_1Q,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2022,4,2),  datetime(2022,5,18), Rebalancing,Fee_M)
    df_ALL_2022_2Q, Balance = Asset_Rebalancing(Universe2022_2Q,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2022,5,19), datetime(2022,8,18), Rebalancing,Fee_M)
    df_ALL_2022_3Q, Balance = Asset_Rebalancing(Universe2022_3Q,round(((Balance*(100-End_of_Q_Reval_Fee))/100),1),datetime(2022,8,19), datetime.now(), Rebalancing,Fee_M)

    df_ALL = pd.concat([df_ALL_2012_1Q,df_ALL_2012_2Q])
    df_ALL = pd.concat([df_ALL,df_ALL_2012_3Q])
    df_ALL = pd.concat([df_ALL,df_ALL_2012_4Q])

    df_ALL = pd.concat([df_ALL,df_ALL_2013_1Q])
    df_ALL = pd.concat([df_ALL,df_ALL_2013_2Q])
    df_ALL = pd.concat([df_ALL,df_ALL_2013_3Q])
    df_ALL = pd.concat([df_ALL,df_ALL_2013_4Q])

    df_ALL = pd.concat([df_ALL,df_ALL_2014_1Q])
    df_ALL = pd.concat([df_ALL,df_ALL_2014_2Q])
    df_ALL = pd.concat([df_ALL,df_ALL_2014_3Q])
    df_ALL = pd.concat([df_ALL,df_ALL_2014_4Q])

    df_ALL = pd.concat([df_ALL,df_ALL_2015_1Q])
    df_ALL = pd.concat([df_ALL,df_ALL_2015_2Q])
    df_ALL = pd.concat([df_ALL,df_ALL_2015_3Q])
    df_ALL = pd.concat([df_ALL,df_ALL_2015_4Q])

    df_ALL = pd.concat([df_ALL,df_ALL_2016_1Q])
    df_ALL = pd.concat([df_ALL,df_ALL_2016_2Q])
    df_ALL = pd.concat([df_ALL,df_ALL_2016_3Q])
    df_ALL = pd.concat([df_ALL,df_ALL_2016_4Q])

    df_ALL = pd.concat([df_ALL,df_ALL_2017_1Q])
    df_ALL = pd.concat([df_ALL,df_ALL_2017_2Q])
    df_ALL = pd.concat([df_ALL,df_ALL_2017_3Q])
    df_ALL = pd.concat([df_ALL,df_ALL_2017_4Q])

    df_ALL = pd.concat([df_ALL,df_ALL_2018_1Q])
    df_ALL = pd.concat([df_ALL,df_ALL_2018_2Q])
    df_ALL = pd.concat([df_ALL,df_ALL_2018_3Q])
    df_ALL = pd.concat([df_ALL,df_ALL_2018_4Q])

    df_ALL = pd.concat([df_ALL,df_ALL_2019_1Q])
    df_ALL = pd.concat([df_ALL,df_ALL_2019_2Q])
    df_ALL = pd.concat([df_ALL,df_ALL_2019_3Q])
    df_ALL = pd.concat([df_ALL,df_ALL_2019_4Q])

    df_ALL = pd.concat([df_ALL,df_ALL_2020_1Q])
    df_ALL = pd.concat([df_ALL,df_ALL_2020_2Q])
    df_ALL = pd.concat([df_ALL,df_ALL_2020_3Q])
    df_ALL = pd.concat([df_ALL,df_ALL_2020_4Q])

    df_ALL = pd.concat([df_ALL,df_ALL_2021_1Q])
    df_ALL = pd.concat([df_ALL,df_ALL_2021_2Q])
    df_ALL = pd.concat([df_ALL,df_ALL_2021_3Q])
    df_ALL = pd.concat([df_ALL,df_ALL_2021_4Q])

    df_ALL = pd.concat([df_ALL,df_ALL_2022_1Q])
    df_ALL = pd.concat([df_ALL,df_ALL_2022_2Q])
    df_ALL = pd.concat([df_ALL,df_ALL_2022_3Q])

    df_ALL = df_ALL.fillna(0)
    
    return df_ALL
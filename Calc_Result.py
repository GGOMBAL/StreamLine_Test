
def Calc_Result(df_ALL):
    
    total_month = len(df_ALL)
    win_month = len(df_ALL[df_ALL['Profit'] >= 0])
    loss_month = len(df_ALL[df_ALL['Profit'] < 0])
    
    print("- In", total_month, "Month, Win Month : ", win_month, "Month", round(win_month/total_month*100,2),"%")
    print("- In", total_month, "Month, Loss Month : ", loss_month, "Month", round(loss_month/total_month*100,2),"%")
    
    # CAGR = (EV / BV)^ (1 / n) - 1
    # BV : 초기값
    # EV : 종료값 = (1+누적수익률) * BV
    # n : 기간 수(연)
    CAGR = ((1+df_ALL['Accumulated_Profit'][-1]/100)**(1/(total_month/12)))-1
    MDD_Date = df_ALL[df_ALL['DrawDown'] == df_ALL['DrawDown'].min()].index.values
    
    print('\n## CAGR : ', round(CAGR*100,2))
    print('## Accumulated Profit : ', round(df_ALL['Accumulated_Profit'][-1],2))
    print('\n## MDD value : ', round(df_ALL['DrawDown'].min(),2))
    print('## MDD month : ', MDD_Date)
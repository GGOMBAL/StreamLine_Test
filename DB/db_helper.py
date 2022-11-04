import sqlite3
import pandas as pd
from Crawling.Get_Price_Data import *
from datetime import date

def check_table_exist(db_name, table_name):
    with sqlite3.connect('{}.db'.format(db_name)) as con:
        cur = con.cursor()
        sql = "SELECT name FROM sqlite_master WHERE type='table' and name=:table_name"
        cur.execute(sql, {"table_name": table_name})

        if len(cur.fetchall()) > 0:
            return True
        else:
            return False


def insert_df_to_db(db_name, table_name, df, option="replace"):
   with sqlite3.connect('{}.db'.format(db_name)) as con:
       df.to_sql(table_name, con, if_exists=option)


def execute_sql(db_name, sql, param={}):
   with sqlite3.connect('{}.db'.format(db_name)) as con:
       cur = con.cursor()
       cur.execute(sql, param)
       cols = [column[0] for column in cur.description]
       results= pd.DataFrame.from_records(data = cur.fetchall(), columns = cols)
       return results

def check_DB_from_drive(Universe, start_day, end_day):
    
    if not check_table_exist('ETF_Data', 'ETF'):
        print('## No DB Crawling from Yahoo.. ##')
        df_DB = get_yahoo_price_data(Universe, start_day, end_day)
        df_DB.index = df_DB.index.values.astype('<M8[m]')
        df_DB.index.name = 'Date'
        df_DB.round(2)
        insert_df_to_db('ETF_Data', 'ETF', df_DB, option="replace")
        print("DB updaate")
    else:
        sql = "select * from ETF"
        df_DB = execute_sql('ETF_Data', sql)
        DB_col_list = list(df_DB)
        df_DB['Date'] = pd.to_datetime(df_DB['index'], infer_datetime_format=True)
        df_DB['Date'] = df_DB["Date"].dt.strftime("%Y-%m-%d")
        df_DB['Date'] = pd.to_datetime(df_DB['Date'], infer_datetime_format=True)  
        df_DB = df_DB.set_index(keys=['Date'], inplace=False, drop=True)
        
        DB_last_time = df_DB.index[-1]
        Current_time = date.today()

        if (not len(Universe) == len(DB_col_list) - 1) or (DB_last_time.month != Current_time.month) or (DB_last_time.day - Current_time.day < -2): # considering index column #
            print('## DB is not newest one, Crawling from Yahoo.. ##')
            df_DB.drop(df_DB.index, inplace=True)
            df_DB.iloc[0:0]    
            
            df_DB = get_yahoo_price_data(Universe, start_day, end_day)
            df_DB.index = df_DB.index.values.astype('<M8[m]')
            df_DB.round(2)
            insert_df_to_db('ETF_Data', 'ETF', df_DB, option="replace")
        else:
            print('## DB is newest One.. ##')
            #df_DB = df_DB.set_index(keys=['Date'], inplace=False, drop=True)
            #df_DB.index.name = 'Date'
            
    sql = "select * from ETF"
    df_DB = execute_sql('ETF_Data', sql)
    df_DB['Date'] = pd.to_datetime(df_DB['index'], infer_datetime_format=True)
    df_DB['Date'] = df_DB["Date"].dt.strftime("%Y-%m-%d")
    df_DB['Date'] = pd.to_datetime(df_DB['Date'], infer_datetime_format=True)

    df_DB = df_DB.set_index(keys=['Date'], inplace=False, drop=True)

    return df_DB

if __name__ == "__main__":
    pass

#with sqlite3.connect("universe_price.db") as conn:
#conn = sqlite3.connect("universe_price.db", isolation_level=None)

#    cur = conn.cursor()

#    sql = "delete from balance where will_clear_at=:will_clear_at"
#    cur.execute(sql, {"will_clear_at": "today"})
#cur.execute('''CREATE TABLE balance
#                (code varchar(6) PRIMARY KEY,
#                bid_price int(20) NOT NULL,
#                quantity int(20) NOT NULL,
#                created_at varchar(14) NOT NULL,
#                will_clear_at varchar(14)
#                )''')

# 데이터 삽입 (INSERT)
#sql = "insert into balance(code, bid_price, quantity, created_at, will_clear_at) values (?, ?, ?, ?, ?)"
#cur.execute(sql, ('001930', 70000, 10, '20201222', 'today'))
#print(cur.rowcount)

# 데이터 조회 (SELECT)
#cur.execute('select * from balance')
#row = cur.fetchone()
#print(row)

#cur.execute('select code, created_at from balance')
#row = cur.fetchall()
#print(row)

#rows = cur.fetchall()
#for row in rows:
#    code, bid_price, quantity, created_at, will_clear_at = row
#    print(code, bid_price, quantity, created_at, will_clear_at)

#sql = "select * from balance where code = :code and created_at = :created_at"
#cur.execute(sql, {"code": '005930', "created_at": '20201222'})

#row = cur.fetchone()
#print(row)

# 데이터 수정 (UPDATE)
#sql = "update balance set will_clear_at=:will_clear_at where bid_price=:bid_price"
#cur.execute(sql, {"will_clear_at": "next", "bid_price": 70000})

#print(cur.rowcount)

# 데이터 삭제 (DELETE)
#sql = "delete from balance where will_clear_at=:will_clear_at"
#cur.execute(sql, {"will_clear_at": "today"})


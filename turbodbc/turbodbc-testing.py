import sqlalchemy
import pandas as pd
import numpy as np
import turbodbc
import credenciais
import time

# 01 - create the table using sqlAlchemy

# 01A - create connection
mydb = 'someDB'


def make_con(db):
    """Connect to a specified db."""
    database_connection = sqlalchemy.create_engine(
        'mssql+pymssql://{0}:{1}@{2}/{3}'.format(
            credenciais.myuser, credenciais.mypassword,
            credenciais.myhost, db
            )
        )
    return database_connection


pd_connection = credenciais.make_con(mydb)


# 01B - load and treat some data - substitute my sample.pkl for yours

df = pd.read_pickle('sample.pkl')

df.columns = df.columns.str.strip()
df = df.applymap(str.strip)
df = df.replace('', np.nan)
df = df.dropna(how='all', axis=0)
df = df.dropna(how='all', axis=1)
df = df.replace(np.nan, 'NA')  # turbodbc hates null values...
df.shape

# 01C - create table using pandas + sqlAlchemy, but just for preparing room for turbodbc

table = 'testing'
df.head().to_sql(table, con=pd_connection, index=False)


# 02 - turbodbc connection

connection = turbodbc.connect(
                                driver="SQL Server",
                                server=credenciais.myhost,
                                database=mydb,
                                uid=credenciais.myuser,
                                pwd=credenciais.mypassword
                            )

# 03 - preparing sql comands and data for turbodbc


def turbo_write(mydb, df, table):
    """Use turbodbc to insert data into sql."""
    start = time.time()
    # preparing columns
    colunas = '('
    colunas += ', '.join(df.columns)
    colunas += ')'

    # preparing value place holders
    val_place_holder = ['?' for col in df.columns]
    sql_val = '('
    sql_val += ', '.join(val_place_holder)
    sql_val += ')'

    # writing sql query for turbodbc
    sql = f"""
    INSERT INTO {mydb}.dbo.{table} {colunas}
    VALUES {sql_val}
    """

    # writing array of values for turbodbc
    valores_df = [df[col].values for col in df.columns]

    # cleans the previous head insert
    with connection.cursor() as cursor:
        cursor.execute(f"delete from {mydb}.dbo.{table}")
        connection.commit()

    # inserts data, for real
    with connection.cursor() as cursor:
        try:
            cursor.executemanycolumns(sql, valores_df)
            connection.commit()
        except Exception:
            connection.rollback()
            print('something went wrong')

    stop = time.time() - start
    return print(f'finished in {stop} seconds')


# 04 - writes data using turbodbc

turbo_write(mydb, df.sample(10000), table)
#  got 10000 lines (77 columns) in 3 seconds

# 05 - pandas method comparison

table = 'pd_testing'


def pandas_comparisson(df, table):
    """Load data using pandas."""
    start = time.time()
    df.to_sql(table, con=pd_connection, index=False)
    stop = time.time() - start
    return print(f'finished in {stop} seconds')


pandas_comparisson(df.sample(10000), table)
# finished in 198 seconds...


# 06 - get versions
turbodbc.__version__
sqlalchemy.__version__
pd.__version__

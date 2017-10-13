import pandas as pd
from pandas import DataFrame
import numpy as np

from common import split


# read a dataframe with NaN from csv file
def get_df_1():
    # NaN and empty data are both treated as NaN
    return pd.read_csv('input/score_with_nan.csv', index_col='name')


# read a dataframe with date format from csv file
def get_df_2():
    return pd.read_csv('input/pv.csv', delimiter=' ', parse_dates=True, index_col='Date')


# read a dataframe from excel file
def get_df_3():
    return pd.read_excel('input/user.xlsx', '2017-sheet', index_col='id')


# handle NaN
def handle_nan():
    df = get_df_1()

    # filter rows with at least one NaN
    df_new = df.dropna(how='any')
    print(df_new)
    split()

    # filter rows with all NaN
    df_new = df.dropna(how='all')
    print(df_new)
    split()

    # fill NaN to a default value
    df_new = df.fillna(value=60)
    print(df_new)
    split()


# write to csv file
def write_to_csv():
    df = get_df_1()

    rows = df.shape[0]
    # add a column, each row value is a random int in [low,high]
    df['art'] = np.random.random_integers(70, 95, rows)
    print(df)
    split()

    print('export score df to csv file')
    # separated by space, 'NaN' to represent NaN value, no headers
    df.to_csv('output/score_with_nan.csv', sep=' ', na_rep='NaN', encoding='utf-8', header=False)


# write to excel
def write_excel():
    df = get_df_3()

    # sort by id
    df.sort_index(inplace=True)

    print(df)
    split()

    print('export user df to excel')
    df.to_excel('output/user.xlsx', sheet_name='2017-sheet', na_rep='', encoding='utf-8', columns=['name', 'job'])


# aggregation
def aggr():
    df = get_df_2()

    # select from year 2015, filter out data before this
    df = df.loc['2015':]
    print(df)
    split()

    # sum rows by year
    df = df.resample('A').sum()  # 'A' means annually
    print(df)
    split()

    # add a column which denotes growth percentage
    df['growth'] = df.pct_change() * 100
    print(df)
    split()


def run():
    # handle_nan()
    # write_to_csv()
    write_excel()
    # aggr()

    pass

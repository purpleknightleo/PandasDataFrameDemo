import pandas as pd
from pandas import DataFrame
import numpy as np


def split():
    print('---------------------------')


# read a dataframe with date format from csv file
def get_df_2():
    return pd.read_csv('input/pv.csv', delimiter=' ', parse_dates=True, index_col='Date')


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
    aggr()

    pass

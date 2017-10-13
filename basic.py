import pandas as pd
from pandas import DataFrame
import numpy as np

from common import split


# construct a dataframe with row/column indices
def get_df_1():
    return DataFrame(np.arange(1, 19).reshape(6, 3), columns=list('abc'),
                     index=pd.Series(['ZJ', 'LN', 'BJ', 'JS', 'SH', 'XJ'], name='Province'))


# display
def display():
    df = get_df_1()

    print(df.info())  # basic info
    split()

    print(df.shape)  # dimension as (n,m), rows = df.shape[0], columns = df.shape[1]
    split()

    print(df.index)  # row index info
    split()

    print(df.columns)  # column index info
    split()

    print(df.head(4))  # first 4 rows
    split()

    print(df.tail())  # last 5 rows
    split()

    print(df.describe())  # basic stats
    split()

    print(df.values)  # all values
    split()


# select rows to new dataframe
def select_rows():
    df = get_df_1()

    # select [1,3) rows by row positions
    df_new = df.iloc[1:3]  # equivalent to df.iloc[1:3,:] or df[1:3] or df.ix[1:3]
    print(df_new)
    print(type(df_new))
    split()

    # select 'LN','BJ' rows by row index labels
    df_new = df.loc[['LN', 'BJ']]
    print(df_new)
    print(type(df_new))
    split()

    # select rows by column values with multiple conditions
    df_new = df.query('b>8 & c<18')  # all rows with value of column 'b' greater than 8 and 'c' less than 18
    print(df_new)
    print(type(df_new))
    split()

    # select rows by column values with multiple conditions
    df_new = df.query('b>14 | c<6')  # all rows with value of column 'b' greater than 14 or 'c' less than 6
    print(df_new)
    print(type(df_new))
    split()


# select columns to new dataframe
def select_columns():
    df = get_df_1()

    # select [1,3) columns by column positions
    df_new = df.iloc[:, 1:3]
    print(df_new)
    print(type(df_new))
    split()

    # select b,c columns by column index labels
    df_new = df.loc[:, ['b', 'c']]
    print(df_new)
    print(type(df_new))
    split()


# select cell
def select_cell():
    df = get_df_1()

    # select a cell by index labels via .at, which is faster than .loc
    a = df.at['JS', 'b']
    print('df["JS"]["b"] = %d' % a)
    split()

    # equivalent to .at, but slower
    a = df.loc['JS', 'b']
    print('df["JS"]["b"] = %d' % a)
    split()

    # select a cell by positions via .iat, which is faster than .iloc
    a = df.iat[3, 1]
    print('df[3][1] = %d' % a)
    split()

    # equivalent to .iloc, but slower
    a = df.iloc[3, 1]
    print('df[3][1] = %d' % a)
    split()


# get row/column position
def get_position():
    df = get_df_1()

    idx_name = 'BJ'
    pos = df.index.get_loc(idx_name)  # get row position by row label
    print('row position of %s = %d' % (idx_name, pos))

    idx_name = 'c'
    pos = df.columns.get_loc(idx_name)  # get column position by column label
    print('column position of %s = %d' % (idx_name, pos))


# drop rows
def drop_rows():
    df = get_df_1()

    # drop rows by row positions
    df_new = df.drop(df.index[[0, 3]])
    print(df_new)
    print(type(df_new))
    split()

    # drop rows by row index labels
    df_new = df.drop(['ZJ', 'JS'])
    print(df_new)
    print(type(df_new))
    split()


# drop columns
def drop_columns():
    df = get_df_1()

    # drop columns by column positions
    df_new = df.drop(df.columns[[0, 2]], 1)  # axis = 1 means column
    print(df_new)
    print(type(df_new))
    split()

    # drop columns by column index labels
    df_new = df.drop(['a', 'c'], axis=1)  # axis = 1 means column
    print(df_new)
    print(type(df_new))
    split()


# change value
def change_val():
    df = get_df_1()

    # change a cell value by index labels
    df.at['JS', 'b'] = 888888  # equivalent to .loc
    print(df)
    split()

    # change a cell value by positions
    df.iat[3, 1] = 888888  # equivalent to .iloc
    print(df)
    split()

    # change value to NaN with conditions
    df.loc[df['b'] > 8, 'a'] = np.nan  # change column 'a' value where column 'b' value greater than 8
    print(df)
    split()

    # apply a function to specified column values
    df['b'] = df['b'].apply(lambda x: x * 10, 1)  # apply() returns series/dataframe, not inplace
    print(df)
    split()


# modify index names/labels
def modify_idx_label():
    df = get_df_1()

    # modify row names
    df.index.set_names('Prov.', inplace=True)

    # modify row index label
    df.rename_axis({'SH': 'HLJ'}, inplace=True)  # default return a new df if inplace is not set
    print(df)
    split()

    # modify column index label
    df.rename_axis({'b': 'B', 'c': 'cc'}, inplace=True, axis=1)
    print(df)
    split()


# sort
def sort():
    df = get_df_1()

    # sort by row index label
    df_new = df.sort_index()
    print(df_new)
    split()

    # sort by row index label in descending order
    df_new = df.sort_index(ascending=False)
    print(df_new)
    split()

    # sort by column index label in descending order
    df_new = df.sort_index(ascending=False, axis=1)
    print(df_new)
    split()

    # sort by column value in descending order
    df_new = df.sort_values('b', ascending=False)
    print(df_new)
    split()


def run():
    # display()
    # select_rows()
    # select_columns()
    # select_cell()
    # get_position()
    # drop_rows()
    # drop_columns()
    # change_val()
    modify_idx_label()
    # sort()

    pass

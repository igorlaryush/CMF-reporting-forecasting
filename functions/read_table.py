import pandas as pd

def read_table(table_path, file=""):
    df = pd.read_excel(table_path, skiprows=28)
    df = df.iloc[:, 8:]
    df.drop(df.tail(49).index,
            inplace=True)

    df = df.set_index('INCOME STATEMENT').transpose()
    cols_to_drop = ['BALANCE SHEET', 'CASH FLOW STATEMENT',
                    'CHANGES TO SHAREHOLDER EQUITY', 'Ratios']
    df.drop(cols_to_drop, axis=1, inplace=True)
    df['Company_name'] = file
    return df

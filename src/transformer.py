from typing import List

import pandas as pd


def df_to_matrix(df: pd.DataFrame, columns: List) -> List:
    list_matrix = []

    for index, row in df.iterrows():
        list_row = []
        for i in columns:
            list_row.append(row[i])
        list_matrix.append(list_row)

    return list_matrix

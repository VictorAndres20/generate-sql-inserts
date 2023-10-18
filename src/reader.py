import pandas as pd
import base64
import io


def read_excel_to_df(path_file: str) -> pd.DataFrame:
    if path_file.endswith('.xlsx'):
        xls = pd.ExcelFile(path_file, engine='openpyxl')
    else:
        xls = pd.ExcelFile(path_file)
    sheet_name = xls.sheet_names[0]
    if sheet_name is None:
        raise Exception('Not sheet name')
    df = pd.read_excel(xls, sheet_name=sheet_name, dtype=str)
    df = df.fillna("")
    return df


def read_excel_from_bytes(bytes_64: str, extension: str) -> pd.DataFrame:
    decrypted = base64.b64decode(bytes_64)
    toread = io.BytesIO()
    toread.write(decrypted)  # pass your `decrypted` string as the argument here
    toread.seek(0)  # reset the pointer
    if extension == 'xlsx':
        df = pd.read_excel(toread, engine='openpyxl')
    else:
        df = pd.read_excel(toread)
    df = df.fillna('')
    return df

from typing import List

from src.reader import read_excel_to_df
from src.transformer import df_to_matrix
from src.writer import write_code


class Generator:

    table_name: str

    def __init__(self, table_name: str, table_schema: str, table_columns: List[dict], excel_columns: List):
        self.table_name = table_name
        self.table_schema = table_schema
        self.table_columns = table_columns
        self.excel_columns = excel_columns
        self.sql = ''

    def build_sql(self, matrix: List):
        for i in matrix:
            self.build_insert_definition()
            self.build_inserts(i)

    def read_excel(self, path: str):
        df = read_excel_to_df(path)
        return df_to_matrix(df, self.excel_columns)

    def build_insert_definition(self):
        self.sql += f"INSERT INTO {self.table_schema + '.' if self.table_schema is not None else ''}{self.table_name}("
        for index in range(0, len(self.table_columns)):
            obj = self.table_columns[index]
            self.sql += f"{obj['key']}"
            if index + 1 != len(self.table_columns):
                self.sql += ','
        self.sql += ') VALUES'

    def build_inserts(self, list_data: List):
        self.sql += '('
        for index in range(0, len(list_data)):
            value = list_data[index]
            metadata = self.table_columns[index]
            self.sql += f"{Generator.validate_str(metadata)}{self.clean_value(value)}{Generator.validate_str(metadata)}"
            if index + 1 != len(list_data):
                self.sql += ','
        self.sql += ');\n'

    @staticmethod
    def clean_value(value: str):
        return str(value).strip().replace('\n', ' ')

    @staticmethod
    def validate_str(metadata: dict):
        if metadata['type'] == 'str':
            return "'"
        return ''

    def write_sql(self, path: str):
        write_code(path, self.sql)


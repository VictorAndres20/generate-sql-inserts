from typing import List

from src.generator import Generator


def generate(source_path: str, table_name: str, table_schema: str, table_columns: List[dict], excel_columns: List, outpu_path: str):
    generator = Generator(table_name, table_schema, table_columns, excel_columns)
    matrix = generator.read_excel(source_path)
    generator.build_sql(matrix)
    generator.write_sql(outpu_path)

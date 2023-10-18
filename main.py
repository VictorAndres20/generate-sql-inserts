from src.controller import generate

''' Change for your needs '''
source_path = '/home/viti/Documents/Freelance/projects/survascun/1.Design/ies_db.xlsx'
table_schema = 'ueb'
table_name = 'ies'
table_columns = [
    {'key': 'uuid', 'type': 'str'},
    {'key': 'name', 'type': 'str'},
    {'key': 'snies', 'type': 'str'},
]
excel_columns = [
    'COD',
    'IES',
    'COD',
]
output_path = '/home/viti/Documents/Freelance/projects/survascun/1.Design/ies_db.sql'


def main():
    generate(source_path, table_name, table_schema, table_columns, excel_columns, output_path)


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

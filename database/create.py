import mysql.connector
from config import dbconfig

tables = \
    {
        'users':
            {
                'user_id': ['integer', 'PRIMARY KEY', 'AUTO_INCREMENT'],
                'chat_id': ['bigint', 'UNIQUE', 'NULL'],
                'subscription': ['integer', 'DEFAULT "10"'],
                'level': ['enum("А1", "А2", "В1", "В2", "С1", "ALL")', 'NULL'],
                'notification': ['text', 'NULL'],
                'hide': ['integer', 'DEFAULT "0"']
            },
        'words':
            {
                'word_id': ['integer', 'PRIMARY KEY', 'AUTO_INCREMENT'],
                'level': ['enum("А1", "А2", "В1", "В2", "С1", "ALL")', 'NULL'],
                'en': ['text', 'NULL'],
                'uk': ['text', 'NULL'],
                'example': ['text', 'NULL']
            },
        'linkage':
            {
                'id': ['integer', 'PRIMARY KEY', 'AUTO_INCREMENT'],
                'user_id': ['integer', 'NULL'],
                'word_id': ['integer', 'NULL'],
                'times': ['integer', 'DEFAULT "1"'],
                'learned': ['enum("0", "1", "2")', 'DEFAULT "0"']
            },
    }


class DatabaseManager:
    def __init__(self, pool_name, pool_size):
        self.pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name=pool_name, pool_size=pool_size, **dbconfig
        )
        self.sql_create_db(dbconfig['database'])

    def sql_create_db(self, database):
        connection = self.pool.get_connection()
        if connection:
            mycursor = connection.cursor()
            mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
            mycursor.execute(f"USE {database}")

            for table_name, table_info in tables.items():
                columns = []
                for column_name, column_info in table_info.items():
                    column_str = f"{column_name} {column_info[0]} {column_info[1]}"
                    if len(column_info) > 2:
                        column_str += f" {column_info[2]}"
                    columns.append(column_str)

                columns_str = ', '.join(columns)
                create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_str})"
                mycursor.execute(create_table_sql)

            mycursor.close()
            connection.close()

from database.create import tables
from database.queries import SQL_QUERIES


class SqlActions:
    def __init__(self, table):
        self.table = table.replace("'", "")
        self.id = tables.get(self.table, None)
        self.mydb = None
        self.mycursor = None

    def __enter__(self):
        from run import dbpool

        self.mydb = dbpool.get_connection()
        self.mycursor = self.mydb.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.mycursor:
            self.mycursor.close()
        if self.mydb:
            self.mydb.close()

    def sql_insert(self, **kwargs):
        columns = ', '.join(kwargs.keys())
        values = ', '.join('%s' for _ in kwargs.values())
        sql = f"INSERT INTO `{self.table}` ({columns}) VALUES ({values})"

        values_tuple = tuple(kwargs.values())

        self.mycursor.execute(sql, values_tuple)
        self.mydb.commit()

    def sql_query(self, **kwargs):
        conditions = []
        values = []

        for key, value in kwargs.items():
            conditions.append(f"{key} = %s")
            values.append(value)

        where_clause = " AND ".join(conditions)
        sql_query = f"SELECT * FROM `{self.table}` WHERE {where_clause}"

        self.mycursor.execute(sql_query, values)
        result = self.mycursor.fetchall()

        return result

    def sql_update(self, cond_column, cond_item, **kwargs):
        changes = ', '.join([f"{key} = %s" for key in kwargs.keys()])
        sql = f"UPDATE `{self.table}` SET {changes} WHERE {cond_column} = %s"

        values = list(kwargs.values())
        values.append(cond_item)

        self.mycursor.execute(sql, values)
        self.mydb.commit()

    def sql_delete(self, cond_column, cond_item):
        sql = f"DELETE FROM `{self.table}` WHERE {cond_column} = %s"

        self.mycursor.execute(sql, (cond_item,))
        self.mydb.commit()

    def sql_query_all(self):
        sql = f"SELECT * FROM `{self.table}`;"

        self.mycursor.execute(sql)
        result = self.mycursor.fetchall()

        return result

    # Special queries
    def execute_sql(self, query_name, *args):
        sql_query, num_params = SQL_QUERIES[query_name]
        if len(args) != num_params:
            raise ValueError(f"Wrong number of args {query_name}")

        self.mycursor.execute(sql_query, args)
        result = self.mycursor.fetchall()
        return result

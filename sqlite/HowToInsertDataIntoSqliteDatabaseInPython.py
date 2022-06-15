# How to insert data into sqlite database in python?
# https://youtu.be/E-BEOD0EPDA

import sqlite3


if __name__ == "__main__":

    local_db_path = "./yt_sqlite.db"
    connection = sqlite3.connect(local_db_path)
    db_cursor = connection.cursor()

    employee = ("Jane", "Smith", 28, "F", 123432323356789)

    # Insert into database
    sql = """INSERT INTO employee(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME)
             VALUES(?,?,?,?,?)"""
    db_cursor.execute(sql, employee)

    connection.commit()
    connection.close()

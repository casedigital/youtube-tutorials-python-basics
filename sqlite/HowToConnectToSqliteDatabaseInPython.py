# How to connect to sqlite database in python?
# https://youtu.be/6faDYCsTXZU

import sqlite3
import pathlib
import os


def method_1(dp_path: str) -> sqlite3.Connection:
    connection = sqlite3.connect(dp_path)
    return connection


def method_2(dp_path: str) -> sqlite3.Connection:
    path_to_db = pathlib.Path(dp_path).absolute().as_uri()
    print(path_to_db)
    connection = None
    try:
        connection = sqlite3.connect(f"{path_to_db}?mode=rw", uri=True)
    except:
        print(
            f"Error trying to open database please check that file exists: {path_to_db}"
        )
        os.sys.exit(1)
    return connection


if __name__ == "__main__":

    local_db_path = "./yt_sqlite.db"
    error_db_path = "DELETE_ME.db"

    # conn = method_1(error_db_path)
    # conn = method_1(local_db_path)
    # conn = method_2(error_db_path)
    conn = method_2(local_db_path)
    cursor = conn.cursor()

    cursor.execute("""SELECT * from EMPLOYEE""")
    result = cursor.fetchall()
    print(result)

    # Closing the connection
    conn.close()

# How to convert string to datetime in python?
import datetime

if __name__ == "__main__":
    date_str = "2023-12-17"

    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    print(date_obj, type(date_obj))
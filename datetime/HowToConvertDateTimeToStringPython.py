# How to convert datetime to string in python?
import datetime

if __name__ == "__main__":
    date_obj = datetime.datetime.now()
    print(date_obj, type(date_obj))
    print('-'*80)

    date_str = str(date_obj)
    print(date_str, type(date_str))
    print('-'*80)

    # month/day/year Hour:Min:Sec
    date_str2 = date_obj.strftime("%m/%d/%Y %I:%M:%S %p")
    print(date_str2, type(date_str2))
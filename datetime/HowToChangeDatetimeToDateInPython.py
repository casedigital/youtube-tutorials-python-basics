# How to change datetime to date in python
import datetime

if __name__ == "__main__":
    cur_datetime = datetime.datetime.now()
    print(f"{cur_datetime = }  {cur_datetime}")
    print('-'*80)

    cur_date = cur_datetime.date()
    print(f"{cur_date = }  {cur_date}")
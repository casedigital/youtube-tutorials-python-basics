# How to check if a string is a number python?

if __name__ == "__main__":
    string_num = ".50"

    print(f"isnumeric: {string_num = } is a number = {string_num.isnumeric()}")
    print(f"isdigit  : {string_num = } is a number = {string_num.isdigit()}")
    print(f"isdecimal: {string_num = } is a number = {string_num.isdecimal()}")

    simplified_num = string_num.replace(".", "").replace("-", "", 1).replace(",", "")
    print(f"replace  : {string_num = } is a number = {simplified_num.isnumeric()}")

    is_number = True
    float_val = None
    try:
        float_val = float(string_num.replace(",", ""))
    except ValueError:
        is_number = False

    print(f"float  : {string_num = }  {float_val = } is a number = {is_number}")

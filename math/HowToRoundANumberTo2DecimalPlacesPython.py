# How to round a number to 2 decimal places in python?
import decimal

if __name__ == "__main__":
    num = 33.64599

    print(round(num, 2), type(round(num, 2)))

    round_str = format(num, ".2f")
    print(round_str, type(round_str), type(float(round_str)))

    print(f"{num:.2f}")

    print(decimal.Decimal(num))
    print(decimal.Decimal(num).quantize(decimal.Decimal("0.00")))

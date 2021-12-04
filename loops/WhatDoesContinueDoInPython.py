# What Does Continue Do In Python?
# https://youtu.be/6Na1_XS_Mpw

if __name__ == '__main__':

    count = 0
    for i in range(10):
        if i == 5:
            continue
        print(f'i = {i}')
        count += i
    
    print(f'count = {count}')

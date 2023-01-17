# How To Check A String For A Character In Python

if __name__ == "__main__":
    test_str = "Hello Youtube"
    print("-" * 80)
    print("Orig: ", test_str)
    print("-" * 80)

    # Method 1: Loops
    for char in test_str:
        if char == "H":
            print(f"Method 1: The letter H has been found")
            break

    # Method 2: in
    # is_found = 'o' in test_str
    if "o" in test_str:
        print(f"Method 2: The letter o has been found using in")

    # Method 3: find
    if test_str.find('o') != -1:
        print(f"Method 3: The letter o has been found using find")

    # Method 4: Count
    if test_str.count('o'):
        print(f"Method 4: The letter o has been found using count")

    # Method 5: any
    if any(char == '!' for char in test_str):
        print(f"Method 5: The letter o has been found using any")
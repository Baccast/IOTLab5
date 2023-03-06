import random


# Color checker method
def color_checker(_input, count):
    # To make the count go 1 to 10 instead of 0 to 9
    count += 1
    # Check for proper color
    if _input in range(-50, -30):
        print(f"{count}. {_input} Blue")
    elif _input in range(-29, -10):
        print(f"{count}. {_input} Green")
    elif _input in range(-9, 10):
        print(f"{count}. {_input} Yellow")
    elif _input in range(11, 30):
        print(f"{count}. {_input} Orange")
    elif _input in range(31, 50):
        print(f"{count}. {_input} Red")


if __name__ == '__main__':
    # Runs the method 10 times
    for x in range(10):
        # Creates random color
        rdm_color = random.randint(-50, 50)
        color_checker(rdm_color, x)

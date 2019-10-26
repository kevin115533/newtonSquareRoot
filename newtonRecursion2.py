import math

def main():
    while True:
        x = input("Enter a positive number or hit Enter to quit: ")
        if x == "":
            exit()
        newton(x, 1)

def newton(x, y):
    number = float(x)
    estimate = 1
    tolerance = 0.000001
    if number == 0:
        return 0
    elif number == 1:
        return 1
    elif number > 1:
        while True:
            estimate = (y + number / y) / 2
            difference = abs(number - y ** 2)
            if difference <= tolerance:
                break
            return newton(number, estimate)
    print("The program's estimate: ", estimate)
    print("Python's estimate:      ", math.sqrt(number))

main()
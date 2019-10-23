import math

def main():
    newton()

def newton():
    while True:
        x = input("Enter a positive number or hit Enter to quit: ")
        if x == "":
            exit()
        number = float(x)
        tolerance = 0.000001
        estimate = 1.0
        while True:
            estimate = (estimate + number / estimate) / 2
            difference = abs(number - estimate ** 2)
            if difference <= tolerance:
                break
        print("The program's estimate: ", estimate)
        print("Python's estimate:      ", math.sqrt(number))

main()

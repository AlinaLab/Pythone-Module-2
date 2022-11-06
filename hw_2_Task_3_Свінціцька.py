fizz = int(input("Введіть число fizz: "))
buzz = int(input("Введіть число buzz: "))
pazz = int(input("Введіть число pazz: "))

def recursive(num):

    if num <= pazz:
        if (num % fizz == 0) and (num % buzz == 0):
            print("FB", end = " ")
        elif num % fizz == 0:
            print("F", end = " ")
        elif num % buzz == 0:
            print("B", end = " ")
        else:
            print(num, end = " ")
        recursive(num + 1)
recursive(1)
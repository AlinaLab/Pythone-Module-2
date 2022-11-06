# Написати алгоритм рішення fizzbuzz для 10 трійок чисел, які записані в файл (file_1.txt).
# 	Читайте із файлу перший рядок, берете із неї числа, рахуйте для них fizzbuzz, виводите.

lst = list()

with open("file_1.txt", encoding="utf-8") as file:
    while True:
        line = file.readline().split()
        if not line:
            break
        i = 1
        while i <= (int(line[-1])):
            if (i % int(line[0]) == 0) and (i % int(line[1]) == 0):
                print("FB", end=" ")
            elif i % int(line[0]) == 0:
                print("F", end=" ")
            elif i % int(line[1]) == 0:
                print("B", end=" ")
            else:
                print(i, end=" ")
            i += 1
        print(sep="\n")
        lst += line
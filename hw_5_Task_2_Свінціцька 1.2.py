lst = list()
# try:
with open("file_2.txt", encoding="utf-8") as file:
    while True:
        # file.seek(0)
        line = file.readline().split()
            # answer = eval(line)
            # fun = line + "=" + answer
            # line = file.write(fun, end="\n")
        if not line:
            break
    # print(sep="\n")
    lst += line
print(lst)
# except ZeroDivisionError:
#     print("Не можна ділити на 0")
#
# def fun(line):
#     answer = eval(line)
#     print(line + "=" + answer)
#
# fun(line)



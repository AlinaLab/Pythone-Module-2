with open("file_2.txt", "r+", encoding="utf-8") as lst:
    line = lst.readlines()
    for i in range(len(line)):
        try:
            line[i] = f'{line[i].rstrip()} = {str(eval(line[i]))}\n'
        except ZeroDivisionError:
            line[i] = f'{line[i].rstrip()} = Error: Не можна ділити на 0\n'
    lst.seek(0)
    [lst.write(el) for el in line]

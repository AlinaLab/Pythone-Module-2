lst = [32, -100, 43, 1, -2, 0, 3, 5, 4, 34, 2.8, -12, 5, 1, 7, 10, 34, 17, 11, 5.1]

for i in range(len(lst)):
    if i % 5 == 0:
        lst[i:(i + 5)] = sorted(lst[i:(i + 5)])
print(lst)
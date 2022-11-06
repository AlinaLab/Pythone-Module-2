year = int(input("Введіть рік: "))
if year % 100 == 0 and year % 400 == 0:
    print("Yes")
elif year % 100 == 0 and year % 400 != 0 and year % 4 == 0:
    print("No")
elif year % 4 == 0:
    print("Yes")
else:
    print("No")
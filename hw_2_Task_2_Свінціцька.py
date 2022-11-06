# Варіант 1
year = int(input("Введіть рік: "))
if year % 100 == 0 and year % 400 == 0:
    print("Yes")
elif year % 100 == 0 and year % 400 != 0 and year % 4 == 0:
    print("No")
elif year % 4 == 0:
    print("Yes")
else:
    print("No")

# Варіант 2 скоротила
year = int(input("Введіть рік: "))
if year % 100 == 0 and year % 400 != 0 and year % 4 == 0:
    print("No")
elif year % 4 == 0 or (year % 100 == 0 and year % 400 == 0):
    print("Yes")
else:
    print("No")

# Варіант 3 ще скоротила
year = int(input("Введіть рік: "))
if (year % 100 != 0 and year % 4 == 0) or (year % 100 == 0 and year % 400 == 0):
    print("Yes")
else:
    print("No")

# Варіант 4 тернарний оператор
year = int(input("Введіть рік: "))
print("No" if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0) else "Yes")

# Варіант 5 булева алгебра
year = int(input("Введіть рік: "))
print((year % 4 != 0 or (year % 100 == 0 and year % 400 != 0)) and "No" or "Yes")

# Варіант 6 булева алгебра зі скороченням "year % 4"
year = int(input("Введіть рік: "))
print((year % 4 or (year % 100 == 0 and year % 400)) and "No" or "Yes")
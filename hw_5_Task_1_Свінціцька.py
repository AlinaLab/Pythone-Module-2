# lst, first_ind, last_ind = [1,10,9,4,5,7,2,0], 2, 6
# lst, first_ind, last_ind = input().split(","), int(input()), int(input())

def fun(lst, first_ind, last_ind):
    if first_ind in range(len(lst)) and last_ind in range(len(lst)):
        lst[first_ind:last_ind] = sorted(lst[first_ind:last_ind])
        print(*lst, sep=",")


fun(input().split(","), int(input()), int(input()))


# Зі списком з умови задачі ([1,10,9,4,5,7,2,0], 2, 6) функція працює.
# Але в мене постійно проблеми з написанням відкритого аргументу для вводу з консолі.
# Наприклад, написала нижче змінну через інпут.
# lst, first_ind, last_ind = input().split(","), int(input()), int(input())
# Але треба в консоль вводити першу змінну у такому вигляді 1,10,9,4,5,7,2,0, а не [1,10,9,4,5,7,2,0].
# Чи це має значення для задачі і якщо так, то як зробити, щоб консоль приймала саме [1,10,9,4,5,7,2,0]?


# Створити функцію як отримує рядок та визначає чи є він Паліндромом.


def check_palindrom(str):
    str = str.lower() # враховувати що літери можуть бути великими і малими, але однаковими за значенням.
    str = str.replace(" ", "").replace("?", "").replace("!", "").replace(".", "").replace(",", "").replace(":", "").replace(";", "").replace('"', "").replace("'", "").replace("-", "").replace("—", "") # Врахувати, що символи розділових знаків і розмітки тексту не враховуються при пошуку паліндрому.
    msg = "паліндром" if str == str[::-1] else "не паліндром"
    print(msg)


str = "І що сало? Ласощі"
# str = str(input())
check_palindrom(str)
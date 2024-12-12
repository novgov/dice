text = input("Введите текст: ")

def count_sumbols(count):
    summ_k = 0
    for k in text:
        if k == count:
            summ_k += 1
    return summ_k

count = input("Какую цифру ищем? ")
sym = input("Какую букву ищем? ")
print("Количество цифр", count, ": ", count_sumbols(count))
print("Количество букв", sym, ": ", count_sumbols(sym))

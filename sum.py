def sumlist(list):
    list = int(list)
    total = sum(list)
    return total
x = (input(("Введите список: ")))

y = x.split()
print("Сумма списка: ", sumlist(list))
def even():
    a = input("Введите число: ")
    sum = 0
    for even in str(a):
        if int(even) % 2==1:
            sum +=1 
    return sum

print("Четность числа(1-не чет, 0-чет): ", even())
def even(a):
    a = input()
    sum = 0
    for even in str(a):
        if int(even) % 2==1:
            sum +=1 
    return sum

print(even(sum))
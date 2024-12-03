def sum_digits(n):
    n = input()
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum
   
print(sum_digits(sum))
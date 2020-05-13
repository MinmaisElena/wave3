import math
n = int(input("Enter an integer(2 ro greater) : "))
if n < 2:
        print("Error: wrong number. Please enter vaild number which is greater than 2.")
def primeFactors(n):
    while n % 2 == 0 and n > 2:
       print(2),
       n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2):
       while n % i== 0:
        print(i)
        n = n / i
    if n > 2:
       print(n)
primeFactors(n)
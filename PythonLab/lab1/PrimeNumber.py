# 2. Find prime numbers between a given range - start(take start no) , end (take end number)

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        return True

num1 = int(input("Enter a number1 : "))
num2 = int(input("Enter a number2: "))

for i in range(num1,num2+1):
    if is_prime(i):
        print(i)
    else:
        pass
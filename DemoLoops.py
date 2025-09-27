num = int(input("Enter a Number - "))
for i in range(2,num):
    if(num %i == 0):
        print("Not a prime number")
        break
else:
    print("Prime Number ")
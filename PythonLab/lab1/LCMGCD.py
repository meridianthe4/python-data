# 6. Find LCM and GCD for given numbers [take 2 numbers] using loops only

def get_hcf(a,b):
    hcf = 1
    if a < b:
        smaller = a
    else:
        smaller = b
    for i in range(1,smaller+1):
        if (a%i==0) and (b%i==0):
            hcf = i

    return hcf

def get_lcm(a,b):
    hcf = get_hcf(a,b)
    return a*b/hcf

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
hcf = get_hcf(num1,num2)
lcm = get_lcm(num1, num2)
print("The HCF of {} and {} is {}".format(num1,num2,hcf))
print("The LCM of {} and {} is {}".format(num1,num2,lcm))
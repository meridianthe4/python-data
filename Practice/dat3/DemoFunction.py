def simple_function():
    print("This is a simple function")

simple_function()

def add(num1,num2):
    return num1 + num2

sum1 = add(5,6)
print(sum1)

sum2 = add(5.9,6.8)
print(sum2)

s1 =add("Vedant","Devre")
print(s1)

def add2(num1:int,num2:int):
    return num1 + num2

a1 = add2(5.6,7.5)
print(a1)

a2 = add((4,5),(5,6))
print(a2)


def calculate_discount(product = 'Table ',price = 9000):
    print(f"Discounted price for {product} is {price * 0.85}")
    

# calculate_discount(900,'Book')  #can't multiply sequence by non-int of type 'float'

'''     Postional Argument  '''
'''
Keyword Argumnent only type not the position at which arg is given is imp
positional argument both the type and position  at which arg is given is imp
'''
calculate_discount('Book',900)
calculate_discount(price=900,product='Book')

'''Default Argument fun can have default values for parameters however when '''

calculate_discount()
calculate_discount('chair')
calculate_discount(price=1000)

'''Varaiable Argument'''

def add(*nums):
    # print(type(nums))
    total = 0
    for num in nums:
        total += num
    
    print(total)
    
numbers = [10,52,1,5,4,6,2,16]
t = (10,20,30,40,50,60)
add(*t)
add(*numbers)
    
'''Var KeyWord Argument'''

def calculate_average(**kwargs):
    print(kwargs)
    values = kwargs['values']
    total = 0
    for val in values:
        total += val
    
    return total/len(values)
    # print(type(kwargs))
    
c1 = calculate_average(name='Adolf' , values = [98,45,21,35,42])
print(f"Avarage marks {c1}")


def print_details(**vedant):
    print(vedant )
    for key,values in vedant.items():
        print(f"{key} : {values}")
        
        
d1 = {'Name ' : 45 , 'Add' : 'New'}
print_details(**d1)
print_details(**{'name':'Vdedant','age' : '22','country' : 'India'})
# 3. Write a python program to swap a 3 digit number
# input 321
# output 123

def swap_number(num):
    if num < 0:
        return -int(str(-num)[::-1])
    return int(str(num)[::-1])

num = int(input("Enter a number: "))
print(f"The number before swapping: {num}")
print(f"The number after swapping: {swap_number(num)}")
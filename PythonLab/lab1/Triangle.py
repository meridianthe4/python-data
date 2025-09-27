# 5. Write a program to check if given triangle is valid if 3 sides of the triangle are provided.
# Also print the type of triangle


def is_right_triangle(a,b,c):
    if a **2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("triangle is right angled triangle")
        return
    print("triangle is not right angled triangle")



def is_triangle(a,b,c):
    if a+b < c or b+c < a or c+a < b:
        print("Not a triangle")
        return
    if a == b == c:
        print("It is an Equilateral triangle.")
    elif a == b or b == c or a == c:
        is_right_triangle(a,b,c)
        print("It is an Isosceles triangle.")
    else:
        is_right_triangle(a,b,c)
        print("It is a Scalene triangle.")

side1 = int(input("Enter side 1: "))
side2 = int(input("Enter side 2: "))
side3 = int(input("Enter side 3: "))
print(f"three sides: {side1}, {side2}, {side3} ")
is_triangle(side1, side2, side3)
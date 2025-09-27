import MathCal

print("Enter Your Choice 1 > Add 2> Sub 3> Mul 4> Division")
ch = int(input())


num1 = int(input("Enter 1st number"))
num2 = int(input("Enter 2nd number"))
match ch:
    case 1:
        num1 = int(input("Enter 1st number"))
        num2 = int(input("Enter 2nd number"))
        MathCal.add(num1,num2)
        pass
    case 2:
        pass
    case 3:
        pass
    case 4:
        pass
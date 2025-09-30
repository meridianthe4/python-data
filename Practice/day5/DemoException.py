import sys,traceback

dividend = int(input("Enter a dividend "))
divisor = int(input("Enter a divisor "))

try :
    result = dividend/divisor
    print(result)
except ZeroDivisionError as e:
    print(e)

except ValueError as e:
    print(e)

else:
    print("Try is succesfullll")

finally :
    print("This will excute always")
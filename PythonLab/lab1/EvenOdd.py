# 4. Count Digits, Even/Odd, Sum
# e.g. 23456
# output digits : 5
# sum : 20
# Even digits : 3
# odd digits :2


def sum_count_EvenOdd(num):
    count = 0
    sum = 0
    even_sum = 0
    odd_sum = 0
    while num > 0:
        digit = num % 10
        if digit % 2 == 0:
            even_sum += 1
        else:
            odd_sum += 1
        sum += digit
        count += 1
        num //= 10
    print(f"No of digits : {count}, Sum of digits : {sum} , Sum of Even digits : {even_sum}, Sum of Odd digits : {odd_sum}")

num = int(input("Enter a number: "))
sum_count_EvenOdd(num)

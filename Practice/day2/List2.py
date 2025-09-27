sq_list = [x**2 for x in range(1,11)]

print(sq_list)

sq_even = [x**2 for x in range(1,11) if x%2 == 0]
print(sq_even)

prices = [780,450,532,452,400,500,700,999]

def calculate_discount(price):
    return price * 0.8

discounted_price = [calculate_discount(price) for price in prices]
print(discounted_price)

words = ['pat','bat','mat',['sat','hat'],'sat','rat','cat','fat']
print(words)
words1 = [word for word in words if not isinstance(word,list)]
print(words1)

for idx,value in enumerate(range(11,21)):
    print(idx+1, " -> ", value , end=" ")

print()


prices = [780,450,532,452,400,500,700,999]

def calculate_discount1(price,discount):
    return price * discount

discount = 0.6
discounted_price = [calculate_discount1(price,discount) for price in prices]
print(discounted_price)


words = ['pat','bat','mat',['sat','hat'],'sat','rat','cat','fat']
print(words)
words2 = [word for word in words if isinstance(word,list)]
print(words2)

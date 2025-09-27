tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127

print(tel)

print(list(tel))
print(sorted(tel))

# tel[4] = 5
# print(tel)
# print(sorted(tel))

print('guido' in tel)
print('guido' not   in tel)

# dict comprehensions
vedant = {x: x**2 for x in (2, 4, 6)}
print(vedant)

sample = {'x': 1, 'y': 2, 'z': 3}

for key in sample:
    print(key, sample[key])      

for key, value in sample.items():
    print(key, value)      

for value in sample.values():
    print(value)              


d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
merged = d1 | d2          
print(merged)


print("=============================================================================")

prices = {
    'apple': 100,'banana': 50, 'cherry': 75
}



def calculate_discount(price):
    return price * 0.8

print(f"Price before the discount {prices}")
discounted_prices = {item: calculate_discount(price) for item, price in prices.items()}

print(f"price after the discount {discounted_prices}")

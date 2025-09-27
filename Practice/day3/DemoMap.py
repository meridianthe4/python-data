numbers = [10,20,33,30,40,50,60,70,80,90,100,11,53,91,57]

def cal_sq(n):
    return n*n

sq = list(map(lambda n: n*n, numbers))
sq1 = list(map(cal_sq,numbers))
print(sq)
print(sq1)

even = list(filter(lambda n : n%2 == 0, numbers))
print(even)


from functools import reduce


min_num = reduce(lambda n1,n2 : n1 if n1<n2 else n2,numbers)
print(min_num)




books = [
    ['Py for Begi', 500 ] , ['Black Book Java', 900 ] , ['C# Book ', 800] , ['AI/ML in python ', 550]
    ]

books.sort()
print(books)

books.sort(key= lambda item : item[1])
print(books)


min_price = min(books)
print(min_price)


min_price = min(books, key= lambda item:item[1])
print(min_price)

max_price = max(books, key = lambda item: item[1])
print(max_price)

filtered = list(filter(lambda it : it[1]>600, books))
print(filtered)


colors_data = [{'Name ' : 'Red' , 'Rating' : 65},
               {'Name ' : 'Yellow' , 'Rating' : 70},
               {'Name ' : 'Blue' , 'Rating' : 45},
               {'Name ' : 'Orange' , 'Rating' : 90},
               {'Name ' : 'Black' , 'Rating' : 80}
               ]

sort_by_rating = sorted(colors_data, key = lambda item: item['Rating'] )
sort_by_rating.reverse()
print(sort_by_rating)

'''Sort by Name '''

colors_data.sort(key=lambda item : item['Name '])
print(colors_data)

filtered = [item for item in books if item[1]>500]
print(filtered)

color_rating = list(map(lambda item: item['Name '] + " " + str(item['Rating']), colors_data))
print(color_rating)

# color_rating = map(lambda item: item['Name '] + " " + str(item['Rating']), colors_data)
# print(next(color_rating))
# print(next(color_rating))  

# map(func, *iterables)
my_pets = ['alfred', 'tabitha', 'william', 'arla']

uppered_pets = list(map(str.upper, my_pets))

print(uppered_pets)

# filter(func, iterable)
dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")

palindromes = list(filter(lambda word: word == word[::-1], dromes))

print(palindromes)


# reduce(func, iterable[, initial])
numbers = [3, 4, 6, 9, 34, 12]

def custom_sum(first, second):
    return first + second

result = reduce(custom_sum, numbers)
print(result)

res = reduce(lambda n1, n2 : n1+n2 , numbers)

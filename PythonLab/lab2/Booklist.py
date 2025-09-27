# Q 5. Create a list of books 
# e.g. booklist =[['Java 8', 700], ['Python for Beginners', 500],....]

booklist = [
    ['Java 8', 700],
    ['Python for Beginners', 500],
    ['Data Science with Python', 1200],
    ['C++ Fundamentals', 650],
    ['Machine Learning', 1500],
    ['Web Development with Django', 800]
]

# Perform following operations on the list
# 1. Add a new book with price

booklist.append(['Java for Dummies', 750])

# 2. Remove entry for a book

booklist.pop(6)

# 3. update price for a book 

booklist[1][1] = 550

# 4. Sort the list by book names

# booklist.sort()
# print(booklist)

# 5. Sort the list by prices

# for book in booklist:
#     book[0], book[1] = book[1], book[0]
# booklist.sort()
# for book in booklist:
#     book[0], book[1] = book[1], book[0]
# print(booklist)

updated_booklist = []
for book in booklist:
    if updated_booklist == []:
        updated_booklist.append(book)
    else:
        if updated_booklist[0][1] > book[1]:
            updated_booklist.insert(0, book)
        else:
            updated_booklist.append(book)
print(updated_booklist)

# 6. Print the book with max and min price [hint : you may use min()/max() functions of python]
minprice = booklist[0][1]
minbook = booklist[0]
maxprice = 0
maxbook = []

for book in booklist:
    if book[1]>maxprice:
        maxbook=book
        maxprice=book[1]
    if book[1]<minprice:
        minbook=book
        minprice=book[1]

# print(maxbook)
# print(minbook)

# print(booklist[0])
# print(booklist[-1])
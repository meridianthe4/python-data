cards = ('Spade','Heart','Club','Diamond')
print(cards)

for item in cards:
    print(item)


print("=============================================================================")
one , two , three , four = cards

print(two)
# print(" FBasjdb vaijsvbjiabd vj")
# print(five)
print('Spade' in cards)

numbers = (1,2,3,4,5,6)
first,*middle,last = numbers
print(first)
print(middle)
print(last)

one,*mid,end = cards
print(one)
print(mid)
print(end)


print("=============================================================================")

t1 = (10,20,30)
t2 = ('one','two','three')

t3 = tuple(zip(t1,t2))
print(t3)

t4 = (10,20,30,40,50)
t5 = ('one','two','three')

t6 = tuple(zip(t4,t5))
print(t6)
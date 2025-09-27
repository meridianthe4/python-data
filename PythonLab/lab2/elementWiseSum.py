# Q.6. Write a Python program to compute element-wise sum of given tuples, using “zip()” function
# Original tuples:
# (1, 2, 3, 4)
# (3, 5, 2, 1)
# (2, 2, 3, 1)
# Element-wise sum of the said tuples:
# (6, 9, 8, 6)

t1 = (1, 2, 3, 4)
t2 = (3, 5, 2, 1)
t3 = (2, 2, 3, 1)

# final = tuple(map(lambda a,b,c : a+b+c,zip(t1,t2,t3)))
# print(final)

final = tuple(map(lambda t: t[0]+t[1]+t[2], zip(t1,t2,t3)))
print(final)

ztemp = tuple(zip(t1, t2, t3))
print(ztemp)
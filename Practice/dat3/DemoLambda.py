def increatment(n):
    return n +1
    
inc = increatment # no round bracket we are assign a function to variable

print(inc(20))

''' Using Lambda ''' '''Short hand notation to define function anonymous'''
inc1 = lambda n : n+1


l0 = lambda : 100
print(l0())

l1 = lambda n1,n2,n3 : n1+n2+n3
print(l1(10,20,30))

l2 = lambda n1,n2,n3 = 6 : n1+n2+n3
print(l2(10,20))

l3 = lambda *args : sum(args)
print(l3(3,5,6,4,8,5,9,4,21,32))

lst = [1,2,3,4,5,6,8,9,8,4,5,21,63,5,2,6,3,5,3,4]
print(l3(*lst))


l4 = lambda **kwargs : sum(kwargs.values())
dic = {}
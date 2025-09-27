# def inc(n):
#     print(id(n))
#     n = n + 1
#     # print(n)
#     # print(id(n))
    

# num = 10
# # print(id(num))
# inc(num)
# print(num)
# print(id(num))


def inc_list(lst):
    lst[0] += 1
    
lst = [10]
inc_list(lst)
print(lst[0])


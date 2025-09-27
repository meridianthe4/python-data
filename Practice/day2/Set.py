set = {'One','Two','Three','Four','Five','Six','Seven','Eight'}

# print(set)

# for i in range(len(set)):
    # print(set(i))

for item in set:
    print(item)

set.add('Ten')

print("=============================================================================")

populated_cities = {'Moscow','Denver','Helsinki','Oslo','Gothenburg','Mumbai','Delhi'}
poluted_cities   = {'Delhi','Karchi','Oslo','Helsinki','Copenhagen'}

inter = poluted_cities.intersection(populated_cities)
print(inter)

'''Using & '''

inter2 = poluted_cities & populated_cities
print(inter2)

''' Differnece '''

print("=============================================================================")

dif1 = populated_cities.difference(poluted_cities)
print(dif1)

# using - 
dif2 = populated_cities - poluted_cities
print(dif2) 


print("=============================================================================")

''' Symmatric Difference '''
dif3 = poluted_cities.symmetric_difference(populated_cities)
print(dif3)

dif4 = poluted_cities ^ populated_cities
print(dif4)
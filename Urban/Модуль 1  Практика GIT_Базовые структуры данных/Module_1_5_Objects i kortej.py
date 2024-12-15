immutable_var = (1, 2, 'a', 'b', True) #кортеж
print(immutable_var)
print(type(immutable_var))

#immutable_var [0] = 3
#print(immutable_var)

mutable_list = ['apple', 'pen', True, 1] #список
print(mutable_list)

mutable_list[0] = 'broad'
print(mutable_list)

mutable_list[3] = 3
print(mutable_list)
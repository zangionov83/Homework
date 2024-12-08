my_dict = {'Alex': 1983, 'Zaira': 1987, 'Alina': 2016, 'Sarmat': 2022}
print(my_dict)

print(my_dict['Alex'])

print(my_dict.get('Victor'))

my_dict.update({'Lira': 1960, 'Sergei': 1982})
print(my_dict)

print(my_dict.get('Lira'))
my_dict.pop('Lira')

print(my_dict)

my_set = {1, 2, 3, 3, 2, 4, 4, 'Alex', 'Zaira', (1, 2, 3,)}
print(my_set)

my_set.update({5, 6})
print(my_set)

my_set.discard(6)
print(my_set)

my_dict = {'Rurik':862, 'Oleg':879, 'Igor':912, 'Olga':945, 'Svyatoslav':945, 'Yaropolk':972}
print(my_dict)
print(my_dict['Olga'])
my_dict['Vladimir'] = 978
print(my_dict['Vladimir'])
my_dict.update({'Yaroslav':1016, 'Putin':1999})
print(my_dict)
del my_dict['Oleg']
print(my_dict)
print(my_dict.get('Oleg'))
my_set = {2, 8, 10, 18, 28,2, 100, 46, 54, 100, 'Фибоначчи', 123.456}
print(my_set)
print(my_set.add(101))
print(my_set.add('Фурье'))
print(my_set)
print(my_set.remove(10))
print(my_set)

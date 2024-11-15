# Работа с словарями
my_dict = {'Andrey' : 2000 , 'Lisa' : 1990, 'Ira' : 1980}
print('Словарь: ', my_dict)
print('Вывод значения: ', my_dict.get('Andrey'))
print('Вывод отсутствующего значения: ', my_dict.get('Ola', 'Такого значения нет'))
my_dict.update ({'Ilia':1985,
               'Anton': 1988})

del my_dict['Lisa']
print('Словарь после изменений: ', my_dict)
# Работа с множествами
my_set = {1, 1, 2, 2, 3, 3, 4, 4, 5, 5}
print('множество:', my_set)
my_set.add(6)
my_set.add(7)
my_set.pop()
print('множество после изменений: ', my_set)
my_dict={'Иван': 1998 , 'Пётр': 2001 ,'Елена': 1978 ,'Оля': 2006}
print(my_dict)
print(my_dict["Иван"])
print(my_dict.get('Андрей' , 'Такого ключа нет'))
my_dict.update({'Alex': 2004 , 'Santa': 1996})
print(my_dict)
my_dict.pop('Елена')
print(my_dict.get('Елена'))
print(my_dict)
# Работа с множествами
my_set={1,2,4,6,4,7,2,7,'Fleg','d','d'}
print(my_set)
my_set.update({9, 'sal'})
print(my_set)
my_set.discard(1)
print(my_set)
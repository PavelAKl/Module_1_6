my_dict = {'Ivan': 1997, 'Sergey': 1988, 'Pavel': 1998, 'Sasha': 1995}
# print(my_dict['Sergey']) # 1st sposob
print(my_dict.get('Sergey')) #2nd sposob
print(my_dict.get('Anna'))
my_dict.update({'Anna': 1994,
                'Elena':1993})
# del my_dict['Anna'] # 1st sposob
a= my_dict.pop('Anna') # 2nd sposob
print(my_dict.get('Elena'))
print(my_dict)


my_set = {1,1,1,1,1,32.23,32.23,'Der','Der', (1,2,3), (1,2,3)}
print(my_set)
my_set.add('Red') , my_set.add(19)
# my_set.discard(1) # 1st sposob
my_set.remove(1) # 2nd sposod
print(my_set)
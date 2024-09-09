#Hellow
my_dict={'Kate':1994, 'Artemy':2021, 'Loki':2019, 'Tosha':2020}
print('Dict:', my_dict)
print('Existing value:', my_dict['Kate'])
print('Not existing value:', my_dict.get('Lena'))
my_dict.update({'Oleg':1970,'anna':1954})
removed_date=my_dict.pop('Kate')
print('Deleted value:', removed_date)
print('Modified dictionary:', my_dict)

#множества
my_set={1,2,1,2,5,6,'cat','dog','cat'}
print('Set:', my_set)
my_set.update(['д', 'о',])
my_set.remove(1)
print('Modified set:', my_set)

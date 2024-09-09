immutable_var=(1, 2.3, 'cat', 'dog')
print(immutable_var)
#print(immutable_var[0]=2) #error потому что нельзя изменить кортеж
mutable_list=[1, 2.3, 5, 'apple', 'Loki']
mutable_list[2]='frog'
mutable_list.remove('Loki')
print(mutable_list)
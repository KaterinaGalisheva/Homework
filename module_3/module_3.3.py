
values_list = [1, 'Kate', False]
values_dict = {'a' : 1, 'b' : 'Kate', 'c' : False}
values_list_2 = [54.32, 'Loki']

def print_params (a = 1, b = 'str', c = True):
    print(a, b, c)

print_params(*values_list)
print_params(**values_dict)
print(*values_list_2, 42)


#Можно передавать вот так(список создаётся локально, мы не влияем на его изменение вне функции)
#def append_to_list(item, list_my=None):
  #if list_my is None:
  # list_my = []
 # list_my.append(item)
#print(list_my)
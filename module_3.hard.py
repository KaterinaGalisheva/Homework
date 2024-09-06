data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum (data_structure):
    num = 0
    if isinstance(data_structure, str):
        num += int(len(data_structure))
    if isinstance(data_structure, int, float):
        num += data_structure
        # здесь нужно закольцевать функцию на типы str или int/float?
    if isinstance(data_structure, list, tuple, set):
        for i in data_structure:
            if i == int or float:
                num += i
            if i == str:
                num += int(len(i))
            # num += calculate_structure_sum(i)
    if isinstance(data_structure, dict):
        for key, value in data_structure.items():
            if i == int or float:
                num += i
            if i == str:
                num += int(len(i))
            #num += calculate_structure_sum(key)
            #num += calculate_structure_sum(value)
    return num




finish = calculate_structure_sum(*data_structure)
print(finish)

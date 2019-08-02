"""
Дан массив a из n целых чисел. Напишите программу, которая найдет число, которое чаще других встречается в массиве.
"""

inp = input().strip()  # входные данные (список чисел)
inp = [int(i) for i in inp.split(' ')]
unique_dict = {i: inp.count(i) for i in inp}  # делаем словарик, так как в нем получаем уникальные элементы ключей

result = list(unique_dict.keys())[0]
for i in unique_dict:
    if i > result:
        result = i
        if unique_dict[i] > unique_dict[result]:
            result = i

print(result)

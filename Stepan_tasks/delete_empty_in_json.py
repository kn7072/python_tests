"""
Напишите программу, которая из JSON-структуры удаляет значения,
 являющиеся пустыми словарями ({}) или пустыми списками ([]), до тех пор, пока есть такие значения.
  Если удаляется значение в словаре, то удаляется и соответствующий ключ.
"""
from json import *

inp = '[[{}], {}, ""]'

decode = loads(inp)

not_empty = False
del_dict_items = 0
del_list_items = 0


def del_list(item, list_items):
    is_del = False
    dict_del = True if item == {} else False
    if type(item) is list:
        i = 0
        while i < len(item):
            if del_list(item[i], item):
                i -= 1
            i += 1
    if type(item) is dict and not dict_del:
        del_dict(item)
    if item == [] or item == {}:
        list_items.remove(item)
        if item == []:
            global del_list_items
            del_list_items += 1
        if item == {}:
            global del_dict_items
            del_dict_items += 1
        is_del = True
    return is_del


def del_dict(dict_items):
    keys = list(dict_items.keys())
    for i in keys:
        fast_del = True if dict_items[i] == [] or dict_items[i] == {} else False
        if type(dict_items[i]) is list and not fast_del:
            j = 0
            while j < len(dict_items[i]):
                if del_list(dict_items[i][j], dict_items[i]):
                    j -= 1
                j += 1
        if type(dict_items[i]) is dict and not fast_del:
            del_dict(dict_items)
        if fast_del:
            if dict_items[i] == []:
                global del_list_items
                del_list_items += 1
            if dict_items[i] == {}:
                global del_dict_items
                del_dict_items += 1
            dict_items.pop(i)


parse_list = loads(input())

i = 0
while i < len(parse_list):
    if del_list(parse_list[i], parse_list):
        i -= 1
    i += 1

if not parse_list:
    del_list_items += 1
    parse_list = None

print(parse_list)
print('Удалено пустых словарей: {0}\nУдалено пустых списков: {1}'.format(del_dict_items, del_list_items))

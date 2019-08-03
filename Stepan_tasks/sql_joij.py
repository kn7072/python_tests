"""
Аналог sql join
Пример 1
Ввод	Вывод
3       1 2 3
1 2     3 4 5
3 4
5 6
3
1 3
3 5
7 9
INNER

"""


def sql_join(table1, table2, action):
    result = []
    tab1_id = [i[0] for i in table1]
    tab2_id = [i[0] for i in table2]
    if action == 'INNER':
        for i in range(len(table1)):
            if table1[i][0] == table2[i][0]:
                result.append(table1[i] + table2[i][1:])
    if action == 'LEFT':
        for i in range(len(table1)):
            if table1[i][0] == table2[i][0]:
                result.append(table1[i] + table2[i][1:])
            else:
                result.append(table1[i] + ['NULL'])
    if action == 'RIGHT':
        for i in range(len(table2)):
            if table2[i][0] == table1[i][0]:
                result.append(table1[i] + table2[i][1:])
            else:
                result.append(table2[i][:1] + ['NULL'] + table2[i][1:])
    if action == 'FULL':
        for i in range(len(table2)):
            if table1[i][0] == table2[i][0]:
                result.append(table1[i] + table2[i][1:])
            if table1[i][0] not in tab2_id:
                result.append(table1[i] + ['NULL'])
            if table2[i][0] not in tab1_id:
                result.append(table2[i][:1] + ['NULL'] + table2[i][1:])
    return ''.join([' '.join(i) + '\n' for i in result])


with open('C:/for_test.txt', 'r') as f:
    table1 = []
    table2 = []
    for i in range(int(f.readline().replace('\n', ''))):
        table1.append(f.readline().replace('\n', '').split(' '))
    for i in range(int(f.readline().replace('\n', ''))):
        table2.append(f.readline().replace('\n', '').split(' '))
    action = f.readline()

result = sql_join(table1, table2, action)
print(result)

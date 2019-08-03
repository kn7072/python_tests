# РЕШЕНИЕ НЕ ПРИНИМАЕТСЯ - ТАКИЕ ЗАДАЧИ РЕКУРСИЕЙ НЕ РАШАЮТСЯ - СЛИШКОМ БОЛЬШАЯ ВЛОЖЕННОСТЬ + КРАЙНЕ НЕ ЭФФЕКТИВНО ВЕДЕТСЯ РАСЧЕТ
"""
Последовательность f0, f1, f2, … задана рекуррентными соотношениями
f0 = 0, f1 = 1, f2 = 2 и fk = fk-1 + fk-3.

Напишите программу, которая вычисляет n элементов этой последовательности c номерами k1, k2, …, kn.
"""


def wrong_fibonachi(item):  # так же как фибоначчи, только другой шаг
    if item == 0 or item == 1 or item == 2:
        return item
    else:
        return wrong_fibonachi(item - 1) + wrong_fibonachi(item - 3)


inp = [int(i) for i in input().split(' ')]
result = []
for i in inp:
    result.append(str(wrong_fibonachi(i)))

print(' '.join(result))

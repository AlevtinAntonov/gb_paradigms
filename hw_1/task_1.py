# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.
# Задача №2
# Написать точно такую же процедуру, но в декларативном стиле
import random


def sort_list_imperarative(numbers):
    for i in range(len(numbers)):
        print(i)
        cursor = numbers[i]
        pos = i
        while pos > 0 and numbers[pos - 1] < cursor:
            numbers[pos] = numbers[pos - 1]
            pos = pos - 1
        numbers[pos] = cursor
    return numbers


def sort_list_declarative(numbers):
    return sorted(numbers, reverse=True)


if __name__ == '__main__':
    print(sort_list_imperarative([0, 22, 10, 5, 42, 3, 0]))
    print(sort_list_declarative([0, 22, 10, 5, 42, 3, 0]))

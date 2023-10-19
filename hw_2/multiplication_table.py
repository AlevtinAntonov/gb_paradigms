# Таблица умножения
# Домашнее задание
# ● Условие
# На вход подается число n.
# ● Задача
# Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
# Обоснуйте выбор парадигм.

def multiplication_table(num):
    mult_tbl = []
    if num < 1:
        return
    for i in range(1, num + 1):
        item = []
        for j in range(1, 10):
            item.append(f'{i} * {j} = {i * j}')
        mult_tbl.append(item)
    return mult_tbl


def print_table(mult_lst: list):
    for row in zip(*mult_lst):
        print('\t'.join(row))


if __name__ == '__main__':
    num = int(input('Введите число: '))
    print_table(multiplication_table(num))

# Написать программу на любом языке в любой парадигме для бинарного поиска. На вход подаётся целочисленный массив и
# число. На выходе - индекс элемента или -1, в случае если искомого элемента нет в массиве.
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == '__main__':
    my_list = [1, 3, 4, 6, 7, 8, 10, 13, 14]
    target_element = 9
    result = binary_search(my_list, target_element)
    if result != -1:
        print(f"Элемент {target_element} найден по индексу {result}.")
    else:
        print(f"Элемент {target_element} не найден в массиве.")

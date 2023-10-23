# Написать скрипт для расчета корреляции Пирсона между двумя случайными величинами (двумя массивами). Можете
# использовать любую парадигму, но рекомендую использовать функциональную, т.к. в этом примере она значительно
# упростит вам жизнь.

import numpy as np

array1 = [1, 2, 3, 4, 5]
array2 = [5, 4, 3, 2, 1]


def pearson_correlation(arr1, arr2):
    mean_arr1 = np.mean(arr1)
    mean_arr2 = np.mean(arr2)
    centered_arr1 = arr1 - mean_arr1
    centered_arr2 = arr2 - mean_arr2

    numerator = np.sum(centered_arr1 * centered_arr2)
    denominator_arr1 = np.sqrt(np.sum(centered_arr1 ** 2))
    denominator_arr2 = np.sqrt(np.sum(centered_arr2 ** 2))

    correlation = numerator / (denominator_arr1 * denominator_arr2)
    return correlation


correlation = pearson_correlation(array1, array2)

print(f"Корреляция Пирсона между массивом 1 и массивом 2: {correlation}")

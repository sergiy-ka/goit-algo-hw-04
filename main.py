# Завдання 1
# Порівняти три різні алгоритми сортування, перевірити їх ефективність на різних наборах даних, використовуючи модуль timeit для вимірювання часу виконання.


import timeit
import random
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from timsort import timsort

if __name__ == "__main__":
    # Створюємо масиви різних розмірів
    data_100 = [random.randint(0, 100) for _ in range(100)]
    data_1000 = [random.randint(0, 1000) for _ in range(1000)]
    data_10000 = [random.randint(0, 10000) for _ in range(10000)]

    # Сортуємо масиви за допомогою вбудованого алгоритму сортування
    timsort_100 = timeit.timeit(lambda: timsort(data_100[:]), number=10)
    timsort_1000 = timeit.timeit(lambda: timsort(data_1000[:]), number=10)
    timsort_10000 = timeit.timeit(lambda: timsort(data_10000[:]), number=10)

    # Сортуємо масиви за допомогою алгоритму сортування злиттям
    merge_sort_100 = timeit.timeit(lambda: merge_sort(data_100[:]), number=10)
    merge_sort_1000 = timeit.timeit(lambda: merge_sort(data_1000[:]), number=10)
    merge_sort_10000 = timeit.timeit(lambda: merge_sort(data_10000[:]), number=10)

    # Сортуємо масиви за допомогою алгоритму сортування вставками
    insertion_sort_100 = timeit.timeit(lambda: insertion_sort(data_100[:]), number=10)
    insertion_sort_1000 = timeit.timeit(lambda: insertion_sort(data_1000[:]), number=10)
    insertion_sort_10000 = timeit.timeit(
        lambda: insertion_sort(data_10000[:]), number=10
    )

    # Виводимо результати
    print(f"| {'-'*15:^15} | {'-'*15:^15} | {'-'*15:^15} | {'-'*15:^15} |")
    print(
        f"| {'Розмір масиву':^15} | {'Merge sort':^15} | {'Insertion sort':^15} | {'Timsort':^15} |"
    )
    print(f"| {'-'*15:^15} | {'-'*15:^15} | {'-'*15:^15} | {'-'*15:^15} |")
    print(
        f"| {'100':^15} | {merge_sort_100:^15.10f} | {insertion_sort_100:^15.10f} | {timsort_100:^15.10f} |"
    )
    print(
        f"| {'1000':^15} | {merge_sort_1000:^15.10f} | {insertion_sort_1000:^15.10f} | {timsort_1000:^15.10f} |"
    )
    print(
        f"| {'10000':^15} | {merge_sort_10000:^15.10f} | {insertion_sort_10000:^15.10f} | {timsort_10000:^15.10f} |"
    )
    print(f"| {'-'*15:^15} | {'-'*15:^15} | {'-'*15:^15} | {'-'*15:^15} |")

    # Висновок
    print(
        """Висновок:
          З результатів виконання програми видно, що алгоритм сортування злиттям є швидшим за алгоритм сортування вставками, але повільнішим за вбудований алгоритм сортування Timsort.
          Це пов'язано з тим, що алгоритм сортування злиттям та алгоритм Timsort мають складність O(n*log(n)), а алгоритм сортування вставками має складність O(n^2).
          При цьому поєднання сортування злиттям і сортування вставками робить алгоритм Timsort набагато ефективнішим."""
    )

def binary_search(sorted_array, target):
    left = 0
    right = len(sorted_array) - 1
    iterations = 0

    while left <= right:
        mid = (left + right) // 2
        if sorted_array[mid] == target:
            return iterations, sorted_array[mid]
        elif sorted_array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        iterations += 1

    # Якщо елемент не знайдено, повертаємо верхню межу
    if left < len(sorted_array):
        return iterations, sorted_array[left]
    else:
        return iterations, None

# Приклад використання:
sorted_array = [0.1, 0.5, 1.2, 1.7, 2.3, 3.0, 4.5, 5.2, 6.0, 7.1]
target = 2.0

iterations, upper_bound = binary_search(sorted_array, target)
print("Кількість ітерацій:", iterations)
if upper_bound is not None:
    print("Верхня межа:", upper_bound)
else:
    print("Верхня межа не знайдена")

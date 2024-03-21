import timeit

# Зчитуємо тексти з файлів
with open("text1.txt", "r") as file:
    text1 = file.read()

with open("text2.txt", "r") as file:
    text2 = file.read()

# Реалізації алгоритмів пошуку підрядка:
def naive_search(text, pattern):
    occurrences = []
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            occurrences.append(i)
    return occurrences

def bm_search(text, pattern):
    occurrences = []
    # Реалізуйте алгоритм Боєра-Мура тут
    return occurrences

def kmp_search(text, pattern):
    occurrences = []
    # Реалізуйте алгоритм Кнута-Морріса-Прата тут
    return occurrences

def rk_search(text, pattern):
    occurrences = []
    # Реалізуйте алгоритм Рабіна-Карпа тут
    return occurrences

# Підрядки для пошуку
existing_pattern = "pattern"  # Існуючий підрядок
non_existing_pattern = "xyz"  # Неіснуючий підрядок

# Виміряємо час для кожного алгоритму
naive_existing_time = timeit.timeit(lambda: naive_search(text1, existing_pattern), number=100)
naive_non_existing_time = timeit.timeit(lambda: naive_search(text1, non_existing_pattern), number=100)

bm_existing_time = timeit.timeit(lambda: bm_search(text1, existing_pattern), number=100)
bm_non_existing_time = timeit.timeit(lambda: bm_search(text1, non_existing_pattern), number=100)

kmp_existing_time = timeit.timeit(lambda: kmp_search(text1, existing_pattern), number=100)
kmp_non_existing_time = timeit.timeit(lambda: kmp_search(text1, non_existing_pattern), number=100)

rk_existing_time = timeit.timeit(lambda: rk_search(text1, existing_pattern), number=100)
rk_non_existing_time = timeit.timeit(lambda: rk_search(text1, non_existing_pattern), number=100)

# Виведемо результати
print("Текст 1:")
print("Наївний алгоритм для існуючого підрядка:", naive_existing_time)
print("Боєра-Мура для існуючого підрядка:", bm_existing_time)
print("Кнута-Морріса-Прата для існуючого підрядка:", kmp_existing_time)
print("Рабіна-Карпа для існуючого підрядка:", rk_existing_time)
print()
print("Наївний алгоритм для неіснуючого підрядка:", naive_non_existing_time)
print("Боєра-Мура для неіснуючого підрядка:", bm_non_existing_time)
print("Кнута-Морріса-Прата для неіснуючого підрядка:", kmp_non_existing_time)
print("Рабіна-Карпа для неіснуючого підрядка:", rk_non_existing_time)

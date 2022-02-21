from functools import reduce

# вивести послідовність Фібоначі, кількість вказана в знінній,
#   наприклад: x = 10 -> 1 1 2 3 5 8 13 21 34 55
#   (число з послідовності - це сума попередніх двох чисел

def fibonacci(num):
    prev = 0
    current = 1
    result = []
    for i in range(num):
        result.append(current)
        prev, current = current, current + prev
    print(result)


fibonacci(10)


# порахувати кількість парних і непарних цифр числа,
#   наприклад: х = 225688 -> п = 5, н = 1;
#          х = 33294 -> п = 2, н = 3

def count_even_odd(num):
    even = 0
    odd = 0
    while num > 1:
        if num % 10 % 2 == 0:
            even += 1
        else:
            odd += 1
        num = num // 10
    print('even: ', even, 'odd: ', odd)


count_even_odd(33294)


# прога, що виводить кількість кожного символа з введеної строки,
# наприклад:
# st = 'as 23 fdfdg544'  # введена строка
#
# 'a' -> 1  # вивело в консолі
# 's' -> 1
# ' ' -> 2
# '2' -> 1
# '3' -> 1
# 'f' -> 2
# 'd' -> 2
# 'g' -> 1
# '5' -> 1
# '4' -> 2

def count_symbols(str):
    symbols = {}
    for symb in str:
        if symb not in symbols:
            symbols[symb] = 1
        else:
            symbols[symb] += 1
    for key, value in symbols.items():
        print(f"'{key}' -> {value}")


count_symbols('as 23 fdfdg544')


# генерируем лист с непарных чисел в порядке возрастания [1,3,5,7,9.....n]
# задача сделать c него лист листов такого плана:

# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]  => [ [1], [3,5], [7,9,11], [13,15,17,19] ]
# [1, 3, 5, 7, 9, 11] => [[1], [3, 5], [7, 9, 11]]
# [1, 3, 5, 7, 9]  => [ [1], [3,5], [7,9]]
# [1, 3, 5, 7, 9, 11, 13]  => [[1], [3, 5], [7, 9, 11], [13]]

def generate_odd_list(limit):
    return [i for i in range(1, limit + 1, 2)]


def transform_list(list):
    start = 0
    quant = 1
    result = []

    while True:
        if len(list) < start + quant:
            result.append(list[start:])
            break
        else:
            result.append(list[start: start + quant])
            if result[quant - 1][quant - 1] == list[-1]:
                break
        start += quant
        quant += 1
    return result


print(transform_list(generate_odd_list(17)))

# Дан массив целых чисел, найдите тот, который встречается нечетное количество раз.
# // Всегда будет только одно целое число, которое встречается нечетное количество раз
# //     [1,2,3,4,5,2,4,1,3] -> 5

def find_odd_occurency(list):
    return [i for i in list if list.count(i)%2 == 1][0]


print(find_odd_occurency([1, 2, 3, 4, 5, 2, 4, 1, 3]))

# // Знайти анаграму.
# //     Перевірити чи слово має в собі такі самі літери як і поеперднє слово.
# //
# //     ANAGRAM | MGANRAA -> true
# // EXIT | AXET -> false
# // GOOD | GOOD -> true

def check_anagrams(str1, str2):
    list1 = [i for i in str1]
    list2 = [i for i in str2]
    list1.sort()
    list2.sort()
    return list1 == list2


print(check_anagrams('GOOD', 'GOOD'))

# Точная степень двойки
# // Дано натуральное число N.
# //     Выведите слово YES, если число N является точной степенью двойки, или слово NO в противном случае.
# //     Операцией возведения в степень пользоваться нельзя!

def is_power_of_2(num):
    while num > 2:
        num = num / 2
    if num == 2:
        print("YES")
    else:
        print("NO")

is_power_of_2(1024)

# Сумма цифр числа
# // Дано натуральное число N. Вычислите сумму его цифр.
# //     При решении этой задачи нельзя использовать строки,
# //     списки, массивы ну и циклы, разумеется.
# //     Рекурсія)

def calc_sum_of_digits(num, interim_sum = 0):
    if num >= 1:
        interim_sum += num % 10
        num = num // 10
        return calc_sum_of_digits(num, interim_sum)
    return interim_sum

print(calc_sum_of_digits(12345))

# Палиндром
# // Дано слово, состоящее только из строчных латинских букв. Проверьте, является ли это слово палиндромом. Выведите YES или NO.
# //     При решении этой задачи нельзя пользоваться циклами, в решениях на питоне нельзя использовать срезы с шагом, отличным от 1.

def is_palindrom(str):
    list_copy = list(str).copy()
    list_copy.reverse()

    if list(str) == list_copy:
        return True
    else:
        return False


print(is_palindrom('rotor'))



# Количество единиц
# // Дана последовательность натуральных чисел  в строке, завершающаяся двумя числами 0 подряд.
# // Определите, сколько раз в этой последовательности встречается число 1. Числа, идущие после двух нулей, необходимо игнорировать.
# //
# // 2176491947586100 -> 3

def count_ones(num):
    actual = num.split('00')[0]
    return actual.count('1')

print(count_ones('21764919475861001111'))

# Вирівняти багаторівневий масив в однорівневий
# //     [1,3, ['Hello, 'Wordd', [9,6,1]], ['oops'], 9] -> [1, 3, 'Hello, 'Wordd', 9, 6, 1, 'oops', 9]
# // flat використовувати заборонено.

def custom_flat(arr, path = None):
    if not path:
        path = []
    for i in arr:
        if isinstance(i, list):
            custom_flat(i, path)
        else:
            path.append(i)
    return path

print(custom_flat([1,3, ['Hello', 'Wordd', [9,6,1]], ['oops'], 9]))


#  Знайти набільший елемент в масиві за допомогою reduce
# //     [1,6,9,0,17,88,4,7] -> 88


def find_max(arr):
    return reduce(lambda a, b: a if a > b else b, arr)

print(find_max([1,6,9,0,17,88,4,7]))
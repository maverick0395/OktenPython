# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

def extract_numbers(input):
    return ','.join(el for el in input if el.isdigit())


print(extract_numbers(input('Enter your string: ')))

print('-------------------------------------------------------')


# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі

def extract_exact_numbers(input):
    result = []
    partial_result = ''
    for el in range(len(input)):
        if input[el].isdigit():
            partial_result += input[el]
            if el == len(input) - 1:
                result.append(partial_result)
        else:
            if partial_result:
                result.append(partial_result)
            partial_result = ''

    print(','.join(result))


extract_exact_numbers(input('Enter your string: '))

print('-------------------------------------------------------')


# list comprehension
#
# 1)есть строка:
# greeting = 'Hello, world'
# записать каждый символ в лист поменяв его на верхний регистр
# пример:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

greeting = 'Hello, world'
result = [el.upper() for el in greeting]
print(result)

print('-------------------------------------------------------')


# 2) с диапазона от 0-50 записать в лист только не парные числа, при этом возвести их в квадрат
# пример:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

result2 = [el ** 2 for el in range(50) if el % 2 != 0]
print(result2)

print('-------------------------------------------------------')

# function
#
# - створити функцію яка виводить ліст

def print_list(list):
    print(list)


print_list([3, 4, 2, 5, 1, 5])

print('-------------------------------------------------------')

# - створити функцію яка приймає три числа та виводить та повертає найменьше.

def find_least(a, b, c):
    print(min(a, b, c))
    return min(a, b, c)


find_least(4, 9, 1)

print('-------------------------------------------------------')

# - створити функцію яка приймає три числа та виводить та повертає найбільше.

def find_greatest(a, b, c):
    print(max(a, b, c))
    return max(a, b, c)


find_greatest(4, 9, 1)

print('-------------------------------------------------------')

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше

def return_least_print_greatest(*args):
    print(max(args))
    return min(args)


return_least_print_greatest(4, 1, 6, 8, 10)

print('-------------------------------------------------------')

# - створити функцію яка повертає найбільше число з ліста

def return_greatest(list):
    return max(list)


print(return_greatest([5, 2, 8, 11, 3]))

print('-------------------------------------------------------')

# - створити функцію яка повертає найменьше число з ліста

def return_least(list):
    return min(list)


print(return_least([5, 2, 8, 11, 3]))

print('-------------------------------------------------------')

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.

def sum_of_list(list):
    return sum(list)


print(sum_of_list([5, 2, 8, 11, 3]))

print('-------------------------------------------------------')

# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

def average_of_list(list):
    return sum(list) / len(list)


print(average_of_list([5, 2, 8, 11, 3]))

print('-------------------------------------------------------')

# 1)Дан лист:
#   list = [22, 3,5,2,8,2,-23, 8,23,5]
#   - найти min число в листе
#   - удалить все дубликаты в листе
#   - заменить каждое четвертое значение на "Х"
list2 = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5, 18]


def custom_func1(target_list):
    print('Min: ', min(target_list))
    result = []
    for el in target_list:
        if el not in result:
            result.append(el)
    for i in range(3, len(result), 4):
        result[i] = 'X'
    return result


print(custom_func1(list2))

print('-------------------------------------------------------')

# 2)вывести на экран пустой квадрат из "*" сторона которого указана в переменой:

def build_square(a):
    square = []
    for i in range(a):
        if i == 0 or i == a - 1:
            line = '*' * a
        else:
            line = '*' + ' ' * (a - 2) + '*'
        square.append(line)
    for line in square:
        print(line)


build_square(10)

print('-------------------------------------------------------')

# 3) вывести табличку умножения с помощью цикла while
i = 1
while i < 10:
    for k in [i*j for j in range(1,10)]:
        print(k if k >= 10 else f"{k} ", end=" ")
    print('')
    i += 1


print('-------------------------------------------------------')

# 4) переделать первое задание под меню с помощью цикла
def menu_func(target_list):
    while True:
        print('1. Find the smallest number in list')
        print('2. Delete duplicates from list')
        print('3. Replace every 4th element with "X"')
        print('4. Exit')

        choice = input("Enter your choice: ")

        if choice == '1':
            print('Min: ', min(target_list))
        elif choice == '2':
            result = []
            for el in target_list:
                if el not in result:
                    result.append(el)
            print('List without duplicates: ', result)
        elif choice == '3':
            for i in range(3, len(target_list), 4):
                target_list[i] = 'X'
            print('Added X', target_list)
        elif choice == '4':
            break
        else:
            print('Wrong input, try again')

menu_func([22, 3, 5, 2, 8, 2, -23, 8, 23, 5, 18])


print('-------------------------------------------------------')

# ***  - вывести элемент листа, значение которого ближе всего к среднему арифметическому всех элементов этого же листа
# пример:
# [1, 2, 3, 4, 5, 6, 7, 8, 9] => 5
# [-1, -2, 3, 4, 555] => 4
# [5, 5, 5, 5] => 5
# [-10, 5, 5] => 5

def find_closest_to_average(list):
    avg = sum(list)/len(list)
    closest = max(list)
    for i in list:
        if abs(avg - i) < abs(avg-closest):
            closest = i
    return closest

print(find_closest_to_average([-1, -2, 3, 4, 555]))




from typing import Callable

# написать функцию на замыкания которая будет в себе хранить лист дел, вам нужно реализовать два метода
# - первый записывает в эту переменную запись
# - второй возвращает все записи
#
# запишите 5 тудушек
# и выведете все

# +

# 2) протипизировать первое задание


def notebook() -> tuple[Callable[[dict[str, bool]], None], Callable[[], list[dict]]]:
    todo_list: list[dict] = []

    def add_todo(todo: dict[str, bool]) -> None:
        todo_list.append(todo)

    def get_all() -> list:
        return todo_list

    return add_todo, get_all


todo1 = notebook()
add_todo1 = todo1[0]
add_todo1({"todo": "do homework", "fulfilled": False})
add_todo1({"todo": "do classwork", "fulfilled": False})
add_todo1({"todo": "do sports", "fulfilled": False})
add_todo1({"todo": "do chill", "fulfilled": False})
add_todo1({"todo": "do sleep", "fulfilled": False})

show_todo1 = todo1[1]()

for todo in show_todo1:
    print(todo)


# 3) создать функцию которая будет возвращать сумму разрядов числа в виде строки (тоже с типизацией)
#
# Пример:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'


def get_digit_order(num: int) -> str:
    digits: list[int] = []
    str_digits: list[str] = []
    while num >= 1:
        digits.insert(0, num % 10)
        num = num // 10
    for i in range(0, len(digits)):
        if digits[i] != 0:
            str_digits.append(str(digits[i] * (10**(len(digits) -1 - i))))
    return '+'.join(str_digits)


print(get_digit_order(70304))



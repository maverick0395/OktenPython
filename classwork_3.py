# Создать класс Rectangle:
class Rectangle:
    # -конструктор принимает две стороны x,y
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.square = x*y

    # -описать арифметические методы:
    #   + сума площадей двух экземпляров класса
    @classmethod
    def square_sum(cls, obj1, obj2 ):
        print(obj1.square + obj2.square)

    #   - разница площадей
    @classmethod
    def square_diff(cls, obj1, obj2):
        print(abs(obj1.square - obj2.square))

    #   == или площади равны
    @classmethod
    def square_is_equal(cls, obj1, obj2):
        if obj1.square == obj2.square:
            return True
        return False

    #   != не равны
    @classmethod
    def square_is_not_equal(cls, obj1, obj2):
        if obj1.square != obj2.square:
            return True
        return False

    #   >, < меньше или больше
    @classmethod
    def square_is_greater(cls, obj1, obj2):
        if obj1.square > obj2.square:
            return True
        return False

    @classmethod
    def square_is_less(cls, obj1, obj2):
        if obj1.square < obj2.square:
            return True
        return False

    #   при вызове метода len() подсчитывать сумму сторон
    def __len__(self):
        return self.x + self.y


rect1 = Rectangle(5,4)
print(len(rect1))
rect2 = Rectangle(3,2)

Rectangle.square_diff(rect1, rect2)
Rectangle.square_sum(rect1, rect2)

# создать класс Human (name, age)


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# создать два класса Prince и Cinderella:
# у золушки должно быть имя возраст и размер ноги
# класса золушки должна быть переменная count которая будет считать сколько экземпляров класса золушка было создано
# и метод класса который будет показывать это количество


class Cinderella(Human):
    __count = 0

    def __init__(self, name, age, feet):
        super().__init__(name, age)
        self.feet = feet
        Cinderella.__count += 1

    @staticmethod
    def count_instances():
        return Cinderella.__count

    def __str__(self):
        return self.name


# у принца имя, возраст и размер найденной туфельки, так же должен быть метод который принимает лист золушек и ищет ту самую


class Prince(Human):
    def __init__(self, name, age, feet):
        super().__init__(name, age)
        self.feet = feet

    def find_the_special_one(self, lst):
        for girl in lst:
            if girl.feet == self.feet:
                return girl


pr1 = Prince('Henry', 24, 38)
cd1 = Cinderella('Mia', 18, 39)
cd2 = Cinderella('Alice', 19, 40)
cd3 = Cinderella('Hanna', 20, 38)
cind_list = [cd1, cd2, cd3]

print(pr1.find_the_special_one(cind_list))
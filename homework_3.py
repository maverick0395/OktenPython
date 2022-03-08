# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()

from abc import ABC, abstractmethod

class Printable(ABC):

    @abstractmethod
    def print(self):
        pass

# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable

class Book(Printable):
    def init(self, name):
        self.name = name

    def print(self):
        print(self.name)



class Magazine(Printable):
    def init(self, name: str):
        self.name = name

    def print(self):
        print(self.name)

b1 = Book('1984')
b2 = Book('Lord of the Rings')
b3 = Book('Foundation')
b4 = Book('Shantaram')

# 3) Створити свій кастомний Exception

class NonBookMagazineException(Exception):
    pass


# 4) Створити клас Main в якому буде:

class Main:
    # - змінна класу printable_list яка буде зберігати книжки та журнали
    printable_list: list = []

    # - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом Book або Magazine інакше кидати свою кастомну помилку
    def add(self, item):
        if not isinstance(item, Book) and not isinstance(item, Magazine):
            raise NonBookMagazineException
        self.printable_list.append(item)

    # - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
    @classmethod
    def show_all_magazines(cls):
        for item in cls.printable_list:
            if isinstance(item, Magazine):
                item.print()

    # - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу
    @classmethod
    def show_all_books(cls):
        for item in cls.printable_list:
            if isinstance(item, Book):
                item.print()


collection1 = Main()

# 4)всі методи класу Main запускати в try except, приклад:
# try:
#     Main.add(Magazine('Magazine1'))
#     Main.add(Book('Book1'))
#     Main.add(Magazine('Magazine3'))
#     Main.add(Magazine('Magazine2'))
#     Main.add(Book('Book2'))
#
#     Main.show_all_magazineі()
#     print('-' * 40)
#     Main.show_all_bookі()
# except NonBookMagazineException:
#     print('Це не журнал або книжка')
# except Exception as err:
#     print(err)

try:
    collection1.add(b1)
    collection1.add(b2)
    collection1.add(b3)
    collection1.add(b4)
    collection1.add('book')

    collection1.show_all_books()
except NonBookMagazineException:
    print("Current item is not instance of Book or Magazine class")
except Exception as err:
    print(err)

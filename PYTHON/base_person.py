
    # for 016_Import_class

class Person():
    """Создаем человека"""
    def __init__(self, name, age, height):
        """Инициализируем атрибуты человека"""

        self.name = name
        self.age = age
        self.height = height
        self.weight = 100

    def description_person(self):
        """Получение описания человека"""

        description = self.name + ', возраст ' + str(self.age) + ', рост ' + str(self.height) + ', вес ' + str(self.weight)
        print('Нового человека зовут ', description)

    def get_weight(self):
        """Получение веса человека"""

        print('Вес человека: ' + str(self.weight))

    def update_weight(self, kg):
        """Изменение веса человека"""

        self.weight = kg

man = Person('Alex', 30, 180)
man.description_person()
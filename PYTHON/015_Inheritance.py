
    # Наследование - процесс когда 1 класс наследует атрибуты и методы другого

    # Класс, чьи свойства и методы наследуются называется родительским классом или Суперклассом, Предок,

    # класс, который наследует - потомок, или подкласс

    # класс можно не создавать с нуля, а создать на основе существующего

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

class Warrior(Person):
    """Создаем класс воина"""

    def __init__(self, name, age, height):
        """Инициализируем атрибуты класса родителя"""

        super().__init__(name,age, height)
        self.rage=100

    def get_rage(self):
        """Получение заряда ярости"""

        print('Заряд ярости равен: ' + str(self.rage))

    def description_person(self):
        """Переопределение метода родителя"""

        description = self.name + ', возраст ' + str(self.age) + ', заряд ярости ' + str(self.rage)
        print('Нового человека зовут ' + description)
        


warrior = Warrior('Конан', 32, 200)
# warrior.update_weight(150)
# warrior.description_person()
# warrior.get_rage()
warrior.description_person()
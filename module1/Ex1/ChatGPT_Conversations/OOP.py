#Class

class Car:
    def __init__(self, color):
        self.color = color
    
    def drive(self):
        return "Врум-врум!"

# Тепер ми можемо створювати машинки з цієї інструкції
car1 = Car("Червоний")
car2 = Car("Синій")

print(car1.color)  # Виведе: Червоний
print(car2.drive())  # Виведе: Врум-врум!

#Incapsulation

class Car:
    def __init__(self, color, engine_power):
        self.color = color
        self.__engine_power = engine_power  # Прихований двигун
    
    def get_engine_power(self):
        return self.__engine_power

car = Car("Зелений", 100)
print(car.color)  # Виведе: Зелений
print(car.get_engine_power())  # Виведе: 100


#Inheritance
class Car:
    def __init__(self, color):
        self.color = color
    
    def drive(self):
        return "Врум-врум!"

class RacingCar(Car):
    def race(self):
        return "Гоночна машинка їде дуже швидко!"

racing_car = RacingCar("Жовтий")
print(racing_car.color)  # Виведе: Жовтий
print(racing_car.drive())  # Виведе: Врум-врум!
print(racing_car.race())  # Виведе: Гоночна машинка їде дуже швидко!


#Polymorphism
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Гав-гав!"

class Cat(Animal):
    def speak(self):
        return "Мяу-мяу!"

def animal_sound(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()

animal_sound(dog)  # Виведе: Гав-гав!
animal_sound(cat)  # Виведе: Мяу-мяу!



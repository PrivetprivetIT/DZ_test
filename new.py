class Animal:
    def speak(self):
        print('Издавать звуки')

class Dog(Animal):
    def speak(self):
        print('Гав-гав!')

class BigDog(Dog):
    def speak(self):
        print('Вау-вау!')

class SmallDog(Dog):
    def speak(self):
        print('Тяв-тяв!')

class ToySmallDog(SmallDog):
    def speak(self):
        print('Игрушка звучит как гав-гав!')

class RobotToySmallDog(ToySmallDog):
    def speak(self):
        print('Рав-рав!')

class BigAngryDog(BigDog):
    def speak(self):
        super().speak()
        print('Очень злой взгляд!!!')
        print('Хмурится!')

class Cat(Animal):
    def _meow(self):
        print('Мяу!')
    def speak(self):
        self._meow()

class SmallCat(Cat):
    def _meow(self):
        print('Мурр...')


animal = Animal()
animal.speak()

dog = Dog()
dog.speak()

big_dog = BigDog()
big_dog.speak()

small_dog = SmallDog()
small_dog.speak()

toy_small_dog = ToySmallDog()
toy_small_dog.speak()

robot_toy_small_dog = RobotToySmallDog()
robot_toy_small_dog.speak()

big_angry_dog = BigAngryDog()
big_angry_dog.speak()

cat = Cat()
cat.speak()

small_cat = SmallCat()
small_cat.speak()

def say_n_times(animal, times):
    for _ in range(times):
        animal.speak()

druzok = BigAngryDog()
say_n_times(druzok, 3)

say_n_times(small_cat, 4)

print('-----------------------')

list_of_animals = [Cat(), Dog(), SmallCat(), BigAngryDog()]

for animal in list_of_animals:
    say_n_times(animal, 2)
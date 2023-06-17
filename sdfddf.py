class Animal:
    type = None
    sound = None

    def make_sound(self):
        print(self.sound)

    def __str__(self):
        return f'I am a {self.type}. I {self.sound}.'


class Dog(Animal):
    sound = 'bark'
    type = 'dog'


class Cat(Animal):
    sound = 'meow'
    type = 'cat'


dog = Dog()
cat = Cat()
dog.make_sound()
cat.make_sound()
print(cat)
print(dog)
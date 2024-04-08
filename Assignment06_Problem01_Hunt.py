class Animal():
    def __init__(self, name):
        self.name = name

    def eat(self):
        raise NotImplementedError("Abstract method must be implemented by subclass!")

    def sleep(self, name):
        print("The",self.name,"is sleeping.")

class Mammal(Animal):
    def feed_young(self):
        print("The",self.name,"is feeding its young with milk.")

class Aves(Animal):
    def fly(self):
        print("The",self.name,"is flying.")

class Actinopterygii(Animal):
    def spawn_young(self):
      print("The",self.name,"is spawning its young")

class Dog(Mammal):
    def eat(self):
        print("The dog is eating dog food.")
    
    def bark(self):
        print("The dog goes 'bark bark.'")

class Cat(Mammal):
    def eat(self):
        print("The cat is eating cat food.")
    
    def meow(self):
        print("The cat goes 'meow meow.'")
    

class Eagle(Aves):
    def eat(self):
        print("The eagle eats its prey.")

    def hunt(self):
        print("The eagle hunts and grabs prey with its talons.")
    
class Salmon(Actinopterygii):
    def eat(self):
        print("The salmon eats crustaceans.")

    def salmon_run(self):
        print("The salmon returns back to freshwater, where it was born, to mate.")

dog = Dog("dog")
dog.eat()
dog.feed_young()
dog.bark()

cat = Cat("cat")
cat.eat()
cat.feed_young()
cat.meow()

eagle = Eagle("eagle")
eagle.eat()
eagle.fly()
eagle.hunt()

salmon = Salmon("salmon")
salmon.eat()
salmon.spawn_young()
salmon.salmon_run()



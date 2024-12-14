# Define the Vehicle class
class Vehicle:
    def __init__(self, brand, model):
        """
        Initialize a Vehicle object.

        Args:
            brand (str): Vehicle brand.
            model (str): Vehicle model.
        """
        self.brand = brand
        self.model = model

    def move(self):
        """
        Move the vehicle.
        """
        pass  # To be implemented by subclasses


# Define the Car class (inherits from Vehicle)
class Car(Vehicle):
    def move(self):
        """
        Move the car.
        """
        print(f"Driving a {self.brand} {self.model} 🚗")


# Define the Plane class (inherits from Vehicle)
class Plane(Vehicle):
    def move(self):
        """
        Move the plane.
        """
        print(f"Flying a {self.brand} {self.model} ✈️")


# Define the Animal class
class Animal:
    def __init__(self, name, species):
        """
        Initialize an Animal object.

        Args:
            name (str): Animal name.
            species (str): Animal species.
        """
        self.name = name
        self.species = species

    def move(self):
        """
        Move the animal.
        """
        pass  # To be implemented by subclasses


# Define the Dog class (inherits from Animal)
class Dog(Animal):
    def move(self):
        """
        Move the dog.
        """
        print(f"{self.name} the {self.species} is running 🐶")


# Define the Bird class (inherits from Animal)
class Bird(Animal):
    def move(self):
        """
        Move the bird.
        """
        print(f"{self.name} the {self.species} is flying 🐦")


# Example usage:
if __name__ == "__main__":
    # Create vehicle objects
    car = Car("Toyota", "Camry")
    plane = Plane("Boeing", "747")

    # Create animal objects
    dog = Dog("Buddy", "Dog")
    bird = Bird("Tweety", "Parrot")

    # Move vehicles and animals
    print("Moving vehicles:")
    car.move()
    plane.move()

    print("\nMoving animals:")
    dog.move()
    bird.move()
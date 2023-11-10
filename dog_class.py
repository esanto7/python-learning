class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color
        
    # instance method
    def __str__(self):
            return f"{self.name}'s coat is {philo.coat_color}."
    
    # Another instance method
    def speak(self, sound):
         return f"{self.name} says {sound}."
    
philo = Dog("Philo", 5, "brown")

print(philo)

# print(miles.speak("woof"))
import sys
sys.path.insert(0, "./src")

from textanalysis_tool.animal import Animal, Bird

animal_name = "Jochen"

bird = Bird(name=animal_name)

print(bird.whoami())

animal = Animal("Moose")
print(str(animal))
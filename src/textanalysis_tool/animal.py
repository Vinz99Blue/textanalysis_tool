class Animal:
    def __init__(self, name: str):
        print(f"Creating an Animal named {name}")
        self.name = name

    def __str__(self) -> str:
        return f"I am an Animal. My name is {self.name}."
    
class Bird(Animal):
    def whoami(self) -> str:
        return f"I am a Bird. My name is irrelivant."
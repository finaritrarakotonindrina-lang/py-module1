class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


rose = Plant("Rose", 25.0, 30)
sunflower = Plant("Sunflower", 80.0, 45)
cactus = Plant("Cactus", 15, 120)

print("=== Garden Plant Registry ===")
rose.show()
sunflower.show()
cactus.show()

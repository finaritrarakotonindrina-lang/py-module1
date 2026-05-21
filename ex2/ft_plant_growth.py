class Plant():
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.the_age = age

    def grow(self) -> None:
        self.height = self.height + 0.8

    def age(self) -> None:
        self.the_age = self.the_age + 1

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.the_age} days old")


rose = Plant("rose", 25.0, 30)
print("=== Garden Plant Growth ===")
for i in range(1, 8):
    print(f"=== Day {i} ===")
    rose.grow()
    rose.age()
    rose.show()
print(f"Growth this week: {0.8 * 7:.1f}cm")

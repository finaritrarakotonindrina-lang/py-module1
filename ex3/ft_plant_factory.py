class Plant():
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.the_age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.the_age} days old")


rose = Plant("Rose", 25.0, 30)
oak = Plant("Oak", 200.0, 365)
cactus = Plant("Cactus", 5.0, 90)
sunflower = Plant("Sunflower", 80.0, 45)
fern = Plant("Fern", 15.0, 120)
all_plants = [rose, oak, cactus, sunflower, fern]
print("===  Plant Factory Output ===")
for i in all_plants:
    print("Created: ", end="")
    i.show()

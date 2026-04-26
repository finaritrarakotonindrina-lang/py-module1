class Plant():
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.the_age = age

    def show(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.the_age} days old")


rose = Plant("Rose", 25, 30)
oak = Plant("Oak", 200, 365)
cactus = Plant("Cactus", 5, 90)
sunflower = Plant("Sunflower", 80, 45)
fern = Plant("Fern", 15, 120)
all_plants = [rose, oak, cactus, sunflower, fern]
print("===  Plant Factory Output ===")
for i in all_plants:
    print("Created: ", end="")
    i.show()

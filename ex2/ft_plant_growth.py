class Plant():
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.the_age = age

    def grow(self):
        self.height = self.height + 0.8

    def age(self):
        self.the_age = self.the_age + 1

    def show(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.the_age} days old")


rose = Plant("rose", 25, 30)
print("=== Garden Plant Growth ===")
for i in range(1, 8):
    print(f"=== Day {i} ===")
    rose.grow()
    rose.age()
    rose.show()
print(f"Growth this week: {0.8 * 7:.1f}cm")


class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = float(height)
        self._age_days = int(age)

    def age(self):
        return self._age_days

    def grow(self, cm: float):
        self.height += float(cm)

    def set_age(self, days: int):
        self._age_days = days

    def show(self):
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age()} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        self._is_blooming = False

    def bloom(self):
        self._is_blooming = True

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if self._is_blooming:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float):
        super().__init__(name, height, age)
        self.trunk_diameter = float(trunk_diameter)

    def produce_shade(self):
        print(f"Tree {self.name} now produces a shade of "
              f"{round(self.height, 1)}cm long and "
              f"{round(self.trunk_diameter, 1)}cm wide.")

    def show(self):
        super().show()
        print(f"Trunk diameter: {round(self.trunk_diameter, 1)}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 age: int, harvest_season: str):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow_and_age(self, days: int, growth_cm: float):
        super().grow(growth_cm)
        new_age = super().age() + days
        super().set_age(new_age)
        self.nutritional_value += days

    def show(self):
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print()

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    tomato.grow_and_age(20, 42.0)

    tomato.show()

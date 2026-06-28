class Plant:
    def __init__(self, name: str = "Unknown", height: float = 0.0,
                 starting_age: int = 0, growth_rate: float = 0.1) -> None:
        self._name = name.capitalize()
        if height < 0:
            self._height = 0.0
        else:
            self._height = height
        if starting_age < 0:
            self._age_days = 0
        else:
            self._age_days = starting_age
        self._growth_rate = growth_rate

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age_days

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
        else:
            self._height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
        else:
            self._age_days = age

    def show(self) -> None:
        h = round(self._height, 1)
        if self._age_days == 0 or self._age_days == 1:
            print(f"{self._name}: {h}cm, {self._age_days} day old")
        else:
            print(f"{self._name}: {h}cm, {self._age_days} days old")

    def age(self) -> None:
        self._age_days += 1

    def grow(self) -> None:
        self._height += self._growth_rate


class Flower(Plant):
    def __init__(self, name: str, height: float,
                 starting_age: int, color: str) -> None:
        super().__init__(name, height, starting_age)
        self.color = color
        self.has_bloomed = False

    def bloom(self) -> None:
        self.has_bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.has_bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, starting_age: int,
                 growth_rate: float, trunk_diameter: float = 1.0) -> None:
        super().__init__(name, height, starting_age, growth_rate)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        shade_h = round(self._height, 1)
        shade_w = round(self.trunk_diameter, 1)
        print(f"Tree {self._name} now produces a shade "
              f"of {shade_h}cm long and {shade_w}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {round(self.trunk_diameter, 1)}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 starting_age: int, growth_rate: float,
                 harvest_season: str, nutrition_rate: float) -> None:
        super().__init__(name, height, starting_age, growth_rate)
        self.harvest_season = harvest_season
        self.nutrition_rate = nutrition_rate
        self.nutritional_value = 0.0

    def age(self) -> None:
        super().age()
        self.nutritional_value += self.nutrition_rate

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += self.nutrition_rate
    print()

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value:g}")


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
    oak = Tree("Oak", 200.0, 365, 1.0, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print()

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, 2.1, "April", 0.5)
    tomato.show()
    print("[make tomato grow and age for 20 days]")

    for _ in range(20):
        tomato.grow()
        tomato.age()

    tomato.show()

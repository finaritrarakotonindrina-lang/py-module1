def display_plant_stats(plant: 'Plant') -> None:
    print(f"[statistics for {plant.get_name()}]")
    print(plant.get_stats_summary())


class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow = 0
            self._age = 0
            self._show = 0
            self._shade = 0

        def get_summary(self) -> str:
            return (f"Stats: {self._grow} grow, "
                    f"{self._age} age, {self._show} show")

        def get_shade_summary(self) -> str:
            return f"{self._shade} shade"

    def __init__(self, name: str = "Unknown plant", height: float = 0.0,
                 starting_age: int = 0,
                 growth_rate: float = 0.1) -> None:
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
        self._stats = Plant.Stats()

    @staticmethod
    def is_older_than_a_year(days: int) -> bool:
        return days > 365

    @classmethod
    def create_anonymous(cls) -> 'Plant':
        return cls()

    def get_name(self) -> str:
        return self._name

    def get_stats_summary(self) -> str:
        return self._stats.get_summary()

    def age(self) -> None:
        self._stats._age += 1
        self._age_days += 1

    def grow(self) -> None:
        self._stats._grow += 1
        self._height += self._growth_rate

    def show(self) -> None:
        self._stats._show += 1
        h = round(self._height, 1)
        if self._age_days == 0 or self._age_days == 1:
            print(f"{self._name}: {h}cm, {self._age_days} day old")
        else:
            print(f"{self._name}: {h}cm, {self._age_days} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float,
                 starting_age: int, color: str,
                 growth_rate: float = 8.0) -> None:
        super().__init__(name, height, starting_age, growth_rate)
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
                 growth_rate: float, trunk_diameter: float) -> None:
        super().__init__(name, height, starting_age, growth_rate)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        self._stats._shade += 1
        shade_h = round(self._height, 1)
        shade_w = round(self.trunk_diameter, 1)
        print(f"Tree {self._name} now produces a shade "
              f"of {shade_h}cm long and {shade_w}cm wide.")

    def get_stats_summary(self) -> str:
        base = super().get_stats_summary()
        shade = self._stats.get_shade_summary()
        return f"{base}\n{shade}"

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {round(self.trunk_diameter, 1)}cm")


class Seed(Flower):
    def __init__(self, name: str, height: float,
                 starting_age: int, growth_rate: float,
                 color: str) -> None:
        super().__init__(name, height, starting_age, color, growth_rate)
        self.seed_count = 0

    def bloom(self) -> None:
        super().bloom()
        self.seed_count = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seed_count}")


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    is_30 = Plant.is_older_than_a_year(30)
    print(f"Is 30 days more than a year? -> {is_30}")
    is_400 = Plant.is_older_than_a_year(400)
    print(f"Is 400 days more than a year? -> {is_400}")
    print()
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_plant_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_plant_stats(rose)
    print()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 1.0, 5.0)
    oak.show()
    display_plant_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_stats(oak)
    print()
    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, 30.0, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    display_plant_stats(sunflower)
    print()
    print("=== Anonymous")
    anonymous = Plant.create_anonymous()
    anonymous.show()
    display_plant_stats(anonymous)

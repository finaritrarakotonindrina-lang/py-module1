class Plant:

    class Stats:
        def __init__(self) -> None:
            self.__grow_calls: int = 0
            self.__age_calls: int = 0
            self.__show_calls: int = 0

        def increment_grow(self) -> None:
            self.__grow_calls += 1

        def increment_age(self) -> None:
            self.__age_calls += 1

        def increment_show(self) -> None:
            self.__show_calls += 1

        def display(self) -> None:
            """Affiche les statistiques de base."""
            print(f"Stats: {self.__grow_calls} grow, "
                  f"{self.__age_calls} age, {self.__show_calls} show")

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self._age_days: int = age
        self.stats: Plant.Stats = self.Stats()

    def age(self) -> int:
        self.stats.increment_age()
        return self._age_days

    def grow(self, cm: float) -> None:
        self.stats.increment_grow()
        self.height += cm

    def set_age(self, days: int) -> None:
        self._age_days = days

    def show(self) -> None:
        self.stats.increment_show()
        print(f"{self.name}: {round(self.height, 1)}cm, "
              f"{self._age_days} days old")

    @staticmethod
    def is_older_than_a_year(days: int) -> bool:
        return days > 365

    @classmethod
    def anonymous(cls: type['Plant']) -> 'Plant':
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color
        self._is_blooming: bool = False

    def bloom(self) -> None:
        self._is_blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self._is_blooming:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self.seeds: int = 0

    def bloom_with_seeds(self, seed_count: int) -> None:
        super().bloom()
        self.seeds = seed_count

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")


class Tree(Plant):
    class TreeStats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self.__shade_calls: int = 0

        def increment_shade(self) -> None:
            self.__shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f"{self.__shade_calls} shade")

    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: float = float(trunk_diameter)
        self.stats = self.TreeStats()

    def produce_shade(self) -> None:
        if isinstance(self.stats, Tree.TreeStats):
            self.stats.increment_shade()
        print(f"Tree {self.name} now produces a shade of "
              f"{round(self.height, 1)}cm long and "
              f"{round(self.trunk_diameter, 1)}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {round(self.trunk_diameter, 1)}cm")


def display_plant_analytics(plant_object: Plant) -> None:
    plant_object.stats.display()


def main() -> None:
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_a_year(30)}")
    print(f"Is 400 days more than a year? ->"
          f"{Plant.is_older_than_a_year(400)}")
    print()

    print("=== Flower")
    rose: Flower = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[statistics for Rose]")
    display_plant_analytics(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    display_plant_analytics(rose)
    print()

    print("=== Tree")
    oak: Tree = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[statistics for Oak]")
    display_plant_analytics(oak)

    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    display_plant_analytics(oak)
    print()

    print("=== Seed")
    sunflower: Seed = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.set_age(65)
    _ = sunflower.age()
    sunflower.bloom_with_seeds(42)
    sunflower.show()
    print("[statistics for Sunflower]")
    display_plant_analytics(sunflower)
    print()

    print("=== Anonymous")
    anon_plant: Plant = Plant.anonymous()
    anon_plant.show()
    print("[statistics for Unknown plant]")
    display_plant_analytics(anon_plant)


if __name__ == "__main__":
    main()

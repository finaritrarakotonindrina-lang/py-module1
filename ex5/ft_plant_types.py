class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def show(self) -> None:
        print(f"{self._name}: {round(self._height, 1)}cm, "
              f"{self._age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 leaf_type: str) -> None:
        super().__init__(name, height, age)
        self._leaf_type = leaf_type

    def show(self) -> None:
        super().show()
        print(f"Leaf type: {self._leaf_type}")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_saison: str) -> None:
        super().__init__(name, height, age)
        self._harvest_saison = harvest_saison

    def show(self) -> None:
        super().show()
        print(f"Harvest saeson: {self._harvest_saison}")

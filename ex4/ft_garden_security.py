class Plant():
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        if height < 0:
            self._height = 0.0
        else:
            self._height = height
        if age < 0:
            self._the_age = 0
        else:
            self._the_age = age

    def show(self) -> None:
        print(f"{self._name}: {round(self.get_height(), 1)}cm, "
              f"{self.get_age()} days old")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._the_age

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"\n{self._name}: Error, height can't be negative")
            print("height update rejected")
        else:
            self._height = height
            print(f"\nHeight updated: {self._height}cm")

    def set_age(self, age: int) -> None:
        if (age < 0):
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._the_age = age
            print(f"Age updated: {age}cm")


def main() -> None:
    print("=== Garden Security System ===")

    rose = Plant("Rose", 15.0, 10)
    print("plant created:", end=" ")
    rose.show()

    rose.set_height(25)
    rose.set_age(30)

    rose.set_height(-6)
    rose.set_age(-6)

    print("\nCurrent state:", end=" ")
    rose.show()


if __name__ == "__main__":
    main()

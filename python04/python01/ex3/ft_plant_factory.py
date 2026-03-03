class Plant:
    """class for plant"""
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def message(self) -> None:
        """a method taht prints a message about plants"""
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plants = [("Rose", 25, 30), ("Oak", 200, 365), ("Cactus", 5, 90),
              ("Sunflower", 80, 45), ("Fern", 15, 120)]
    for name, height, age in plants:
        new_plant = Plant(name, height, age)
        new_plant.message()
    print("\nTotal plants created: 5")

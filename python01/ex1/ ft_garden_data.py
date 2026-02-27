class Plant:
    """
    class for Plant
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize the plan with a name a hight"""
        self.name: str = name
        self.height: int = height
        self.age: int = age


if __name__ == "__main__":
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")

    plants = [plant1, plant2, plant3]
    for i in range(3):
        p = plants[i]
        print(f"{p.name}: {p.height}cm, {p.age} days old")

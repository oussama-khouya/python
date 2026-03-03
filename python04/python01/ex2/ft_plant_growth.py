class Plant:
    """class for plant"""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize the plan with a name a hight and age"""
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def grow(self, days: int):
        """a methode that add 1cm for every one day"""
        self.height = self.height + days

    def agee(self, days):
        """a methode that add 1day for every day"""
        self.age = self.age + days

    def get_info(self):
        """a methode that give info about each plant"""
        return f"{self.name}: {self.height}cm, {self.age} days old"


if __name__ == "__main__":
    plant1 = Plant("Rose", 25, 30)
    print("=== Day 1 ===")

    print(plant1.get_info())

    for days in range(6):
        plant1.grow(1)
        plant1.agee(1)

    print("=== Day 7 ===")

    print(plant1.get_info())

    print("Growth this week: +6cm")

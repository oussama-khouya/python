class Plant:
    """ a parent for all classes"""

    def __init__(self, name: str, height: int, age: int) -> None:
        """a methode that init those attr"""
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def get_info(self) -> str:
        """a methode that return info str about the plant"""
        return (f"{self.name} ({self.__class__.__name__}): "
                f"{self.height}cm, {self.age} days")


class Flower(Plant):
    """a child class of plant"""

    def __init__(self, name: str, height: int, age: int, color: int) -> None:
        super().__init__(name, height, age)
        """a super function that call the parnet to inti those attr"""
        self.color: int = color

    def bloom(self) -> None:
        """A methode that print that message for flower class"""
        print(f"{self.name} is blooming beautifully!\n")

    def get_info(self) -> str:
        """ a methode to print info"""
        basic_info = super().get_info()
        return basic_info + f", {self.color}"


class Tree(Plant):
    """ a child class from plant"""

    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        """init those existing attr using super """
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter

    def produce_shade(self) -> None:
        """SHOW THAT MESSAGE FOR THREE"""
        print(f"{self.name} provides 78 square meters of shade\n")

    def get_info(self) -> None:
        basic_info = super().get_info()
        return basic_info + f", {self.trunk_diameter}cm diameter"


class Vegetable(Plant):
    """ A child class from plant"""

    def __init__(self, name: str, height: int, age: int, harvest_season: str):
        """init those existing param using super"""
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season

    def nutritional_value(self) -> None:
        """show that message FOR  vege"""
        print(f"{self.name} is rich in vitamin C")

    def get_info(self) -> None:
        """ SHOW INFO """
        basic_info = super().get_info()
        return basic_info + f", {self.harvest_season}"


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")

    f = Flower("Rose", 25, 30, "red color")
    tr = Tree("Oak", 500, 1825, 50)
    to = Vegetable("Tomato", 80, 90, "summer harvest")

    plant_list = [f, tr, to]

    for i in range(3):
        p = plant_list[i]
        print(p.get_info())

        # isinstance checks if that object is in flower class or others
        if isinstance(p, Flower):
            p.bloom()
        elif isinstance(p, Tree):
            p.produce_shade()
        elif isinstance(p, Vegetable):
            p.nutritional_value()

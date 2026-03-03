# we create classes of all plants we have with its attributes
class Plant:
    """create classes of normal plant"""

    def __init__(self, name: str, height: int) -> None:
        """init its para"""
        self.name: str = name
        self.height: int = height

    def grow(self, cm: int, verbose: bool = True) -> None:
        """grow plant with cm and print only for autorized"""
        self.height = self.height + cm
        if verbose:
            print(f"{self.name} grew {cm}cm")

    def get_info(self) -> None:
        """print info about the plant"""
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """child cls from plant"""

    def __init__(self, name: str, height: int, color: int) -> None:
        """INIT EXisting param using super"""
        super().__init__(name, height)
        self.color = color

    def get_info(self) -> str:
        """show info"""
        basic_info = super().get_info()
        return f"{basic_info}, {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    """clss child of Flwwer plant"""

    def __init__(self, name: str, height: int, color: int,
                 prize_point: int) -> None:
        super().__init__(name, height, color)
        self.prize_point = prize_point

    def get_info(self) -> None:
        """SHOW INFO"""
        basic_info1 = super().get_info()
        return f"{basic_info1}, Prize points: {self.prize_point}"

# we create a GardenManager class that control all other plants


class GardenManager:
    """
    a cls that manage all other classes with
    class variable
    """
    total_gardens = 0

    class GardenStats:
        """we need a math tool to count plant types
        nested static helper"""
        @staticmethod
        def count_types(plants: list) -> tuple:
            """count how many types are for each manager"""
            normal: int = 0
            flowering: int = 0
            prize: int = 0
            for p in plants:
                if isinstance(p, PrizeFlower):
                    prize += 1
                elif isinstance(p, FloweringPlant):
                    flowering += 1
                else:
                    normal += 1
            return normal, flowering, prize

        @staticmethod
        def calculate_score(plants: list) -> int:
            """calculate the score"""
            score: int = 0
            for p in plants:
                score += p.height
                if isinstance(p, PrizeFlower):
                    score += (p.prize_point * 4)
            return score

    def __init__(self, owner: str) -> None:
        """init function for every object built"""
        self.owner: str = owner
        # create an empy list to append to it evry added plant
        self.plants = []
        # calcute every garden is created
        GardenManager.total_gardens += 1

    def add_plant(self, plant: Plant, verbose: bool = True) -> None:
        """adds plant object for each manager"""
        self.plants.append(plant)
        if verbose:
            print(f"added {plant.name} to {self.owner}'s garden")

    def grow_all(self, cm: int, verbose: bool = True) -> None:
        """loop over every plant in list and add it up 1cm"""
        if verbose:
            print(f"{self.owner} is helping all plants grow...")
        for p in self.plants:
            p.grow(cm, verbose=verbose)
    # create a class method to print that message for the whole class

    @classmethod
    def create_garden_network(cls) -> None:
        """class method for the whole class that show"""
        print("=== Garden Management System Demo ===\n")
    # create a function that validate the height

    @staticmethod
    def validate_height(height: int) -> bool:
        """validate the height"""
        return height > 0
    # create a report printing that print that statics

    def report_print(self) -> None:
        """SHOW report for every plant in list"""
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden")
        for p in self.plants:
            print(f"- {p.get_info()}")
        # now we get hwo many types we have
        norm, flow, priz = GardenManager.GardenStats.count_types(self.plants)
        total_plants = len(self.plants)
        print(f"\nPlants added: {total_plants}, Total growth: 3cm")
        print(f"Plant types: {norm} regular, ")
        print(f"{flow} flowering, {priz} prize flowers\n")


if __name__ == "__main__":
    # start the system
    GardenManager.create_garden_network()
    # create alice's garden
    alice = GardenManager("Alice")
    # add diff plants types
    alice.add_plant(Plant("Oak Tree", 100))
    alice.add_plant(FloweringPlant("Rose", 25, "red"))
    alice.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))
    print("\n")
    # grow garden 1cm
    alice.grow_all(1)
    # print the report
    alice.report_print()
    # score validation
    score = GardenManager.GardenStats.calculate_score(alice.plants)
    is_valid = GardenManager.validate_height(10)
    # create bob's garden
    bob = GardenManager("Bob")
    # create plants
    bob.add_plant(Plant("soso", 20,), verbose=False)
    bob.add_plant(FloweringPlant("momo", 20, "blue"), verbose=False)
    bob.add_plant(PrizeFlower("popo", 29, "red", 5), verbose=False)
    # grow bob by 1cm
    bob.grow_all(1, verbose=False)
    # bob is score
    score_b = GardenManager.GardenStats.calculate_score(bob.plants)
    print(f"Height validation test: {is_valid}")
    print(f"Garden scores - Alice: {score}, Bob: {score_b}")
    print(f"Total gardens managed: {GardenManager.total_gardens}")

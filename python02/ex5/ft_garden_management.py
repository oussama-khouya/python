class GardenError(Exception):
    pass
class WaterError(GardenError):
    """
    class that catches all water related errors
    """
    pass
class Name_Error(GardenError):
    """
    class that catches all water related errors
    """
    pass
class Sun_Error(GardenError):
    """
    class that catches all water related errors
    """
    pass

class GardenManager:
    """Class to manage a garden with plants."""

    def __init__(self) -> None:
        self.plants: dict[str, dict[str, int]] = {}

    def add_plants(self, name: str, water: int, sun: int) -> None:
        """Add a plant to the garden, raise Name_Error if name is empty."""
        if not name:
            raise Name_Error(f"Plant name cannot be empty!\n")
        self.plants[name] = {"water": water, "sun": sun}
        print(f"Added {name} successfully")

    def Watering(self, tank_level: int) -> None:
        """
        Water all plants.
        Raises WaterError if tank_level <= 0.
        Uses finally to clean up watering system.
        """
        if tank_level <= 0:
            raise WaterError("Not enough water in tank")

        print("Opening watering system")
        try:
            for plant in self.plants:
                print(f"Watering {plant} - success")
        finally:
            print("Closing watering system (cleanup)\n")

    def check_health(self, name: str) -> None:
        """Check the health of a plant, raise errors if water or sun levels are too high."""
        if name not in self.plants:
            raise Name_Error(f"{name} is not in the Garden")

        if self.plants[name]['water'] > 10:
            raise WaterError(
                f"Error checking {name}: Water level {self.plants[name]['water']} is too high (max 10)"
            )
        if self.plants[name]['sun'] > 12:
            raise Sun_Error(f"Error checking {name}: Sun level {self.plants[name]['sun']} is too high")

        print(f"{name}: healthy (water: {self.plants[name]['water']}, sun: {self.plants[name]['sun']})")

def test_garden_management():
    print("=== Garden Management System ===\n")
    print("Adding plants to garden...")
    alice = GardenManager()
    try:
        alice.add_plants("tomato", 5, 6)
        alice.add_plants("lettuce", 15,4)
        alice.add_plants("", 5,6)
    except Name_Error as e:
        print(f"Error adding plant: {e}")
    print("Watering plants...")
    alice.Watering(5)
    try:
        print("Checking plant health...")
        alice.check_health("tomato")
        alice.check_health("lettuce")
    except WaterError as e:
        print(f"{e}\n")
    try:
        print("Testing error recovery...")
        alice.Watering(0)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    finally:
        print("System recovered and continuing...\n")
    print("Garden management system test complete!")



if __name__ == "__main__":
    test_garden_management()





    
        



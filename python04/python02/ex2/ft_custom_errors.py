class GardenError(Exception):
    """
    class that catches all garden related errors
    """
    pass


class PlantError(GardenError):
    """
    class that catches all plant related errors
    """
    pass


class WaterError(PlantError):
    """
    class that catches all water related errors
    """
    pass


def testErrors() -> None:
    """
    Docstring for testing Errors
    """
    print("=== Custom Garden Errors Demo ===\n")
    try:
        print("Testing PlantError...")
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")
    try:
        print("Testing WaterError...")
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")
    print("Testing catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught a garden error: {e}\n")
    print("All custom error types work correctly!")


if __name__ == "__main__":
    testErrors()

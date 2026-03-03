class SecurePlant:
    """
    a class for secure plants that encapsulate two attributes to protect them
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """a methode that initialize those attributes"""
        self.name: str = name
        self.__height: int = height
        self.__age: int = age

    def get_height(self) -> int:
        """a methode that called getter that get
        the value of that attribute"""
        return self.__height

    def get_age(self) -> int:
        """getter for age"""
        return self.__age

    def set_height(self, height: int) -> None:
        """
        A methode called setter used to set the value of a ecpsulate attr
        """
        if height > 0:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm ")
            print("[REJECTED]\nSecurity: Negative height rejected")

    def set_age(self, age: int) -> None:
        """
        A methode called setter used to set the value of a ecpsulate attr
        """
        if 0 < age < 10000:
            self.__age = age
            print(f"Age updated: {age} days [OK]\n")
        else:
            print(f"Invalid operation attempted: age {age}cm ")
            print("[REJECTED]\nSecurity: Negative age rejected")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant1 = SecurePlant("Rose", 1, 1)

    print(f"Plant created : {plant1.name}")
    plant1.set_height(10)
    plant1.set_age(10)

    plant1.set_height(-5)

    print(f"\nCurrent plant: {plant1.name} ")
    print(f"{plant1.get_height()}cm, {plant1.get_age()} days)")

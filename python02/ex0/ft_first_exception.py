#tem_str = str(input("Testing temperature: "))

def check_temperature(temp_str: str) -> int | None:
    try:
        tem = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")
        return None
    if 0 <= tem <= 40:
        print(f"Temperature {tem}°C is perfect for plants!\n")
        return tem
    elif tem < 0:
        print(f"Error: {tem}°C is too cold for plants (min 0°C)\n")
    else:
        print(f"Error: {tem}°C is too hot for plants (max 40°C)\n")

if __name__ == "__main__":
    def test_temperature_input() -> None:
        print("=== Garden Temperature Checker ===\n")
        temp_list = ["25", "abc", "100", "-50"]
        for temm in temp_list:
            print(f"Testing temperature: {temm}")
            check_temperature(temm)
        print("All tests completed - program didn't crash!")

    test_temperature_input()


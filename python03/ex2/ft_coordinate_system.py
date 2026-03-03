import sys
import math

print("=== Game Coordinate System ===\n")
pos = (10, 20, 5)
a, b, c = pos
dis_zero = math.sqrt(a*a + b*b + c*c)
print(f"Position created: ({a}, {b}, {c})")
print(f"Distance between (0, 0, 0) and {pos}: {dis_zero : .2f}\n")
if len(sys.argv) == 2:
    raw_valid = sys.argv[1]
    print(f'Parsing coordinates: "{raw_valid}"')
    ls = raw_valid.split(",") #list of str
    #convert to list of ints
    loi = []
    try:
        for strs in ls:
            loi.append(int(strs))
        cordinates = tuple(loi)
        x ,y ,z = cordinates
        dis_zero2 = math.sqrt(x**2 + y**2 + z**2)
        print(f"Parsed position: ({x},{y},{z})")
        print(f"Distance between (0, 0, 0) and ({x},{y},{z}): {dis_zero2 : .1f}\n")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f'Error details - Type: ValueError, Args: ("{e}"\n')

    raw_invalid = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{raw_invalid}"')
    invalid_lst = []
    try:
        for m in raw_invalid.split(","):
            invalid_lst.append(int(m))
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f'Error details - Type: ValueError, Args: ("{e}"\n')


    print("Unpacking demonstration:")
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")
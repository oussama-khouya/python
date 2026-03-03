import sys
print("=== Command Quest ===")
total_argument = len(sys.argv)
argument_prov = total_argument - 1

if total_argument > 2:
    print(f"Program name: {sys.argv[0]}")
    print(f"Arguments received: {argument_prov - 1}")
    for i in range(1, total_argument):
        print(f"Argument {i}: {sys.argv[i]}")
    print(f"Total arguments: {total_argument}\n")
elif total_argument == 1:
    print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    print(f"Total arguments: {total_argument}\n")
elif total_argument == 2:
    print(f"Arguments received: {argument_prov}")
    print(f"Argument 1: {sys.argv[1]}")
    print(f"Total arguments: {total_argument}\n")


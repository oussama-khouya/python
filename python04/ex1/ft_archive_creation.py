print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
file_name = "new_discovery.txt"
try:
    file = open(file_name, "w")
    print("Initializing new storage unit: new_discovery.txt")
    print("Storage unit created successfully...\n")
    file.write("[ENTRY 001] New quantum algorithm discovered\n")
    print("[ENTRY 001] New quantum algorithm discovered")
    file.write("[ENTRY 002] Efficiency increased by 347%\n")
    print("[ENTRY 002] Efficiency increased by 347%")
    file.write("[ENTRY 003] Archived by Data Archivist trainee")
    print("[ENTRY 003] Archived by Data Archivist trainee")

finally:
    file.close()
    print("\nData inscription complete. Storage unit sealed.")
print(f"Archive '{file_name}' ready for long-term preservation.")


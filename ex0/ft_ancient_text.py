print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
try:
    file = open("ancient_fragment.txt","r")
    print("Accessing Storage Vault: ancient_fragment.txt")
    print("Connection established...\n")
    print("RECOVERED DATA:")
    print(file.read())
except FileNotFoundError:
    print("ERROR: Storage vault not found")
finally:
    file.close()
    print("\nData recovery complete. Storage unit disconnected.")


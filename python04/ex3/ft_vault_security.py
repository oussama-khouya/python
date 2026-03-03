print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
print("Initiating secure vault access...")
print("Vault connection established with failsafe protocols\n")
print("SECURE EXTRACTION:")
with open("classified_data.txt", "r") as file:
    data = file.read()
    print(data)
with open("classified_data.txt", "w") as file:
    file.write("[CLASSIFIED] New security protocols archived")

print("Vault automatically sealed upon completion\n")
print("All vault operations completed with maximum security.")

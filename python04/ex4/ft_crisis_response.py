def crisis_management(file_name : str, normal : bool) -> None:
    if normal == False:
        first_word = "CRISIS ALERT"
    else:
        first_word = "ROUTINE ACCESS:"

    try:
        print(f"{first_word}: Attempting access to '{file_name}'...")
        with open(file_name, "r") as file:
            data = file.read()
            print(f"SUCCESS: Archive recovered - ``{data}''")
            print("STATUS: Normal operations resumed\n")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")

print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
crisis_management("lost_archive.txt",False)
crisis_management("classified_vault.txt'",False)
crisis_management("standard_archive.tx",True)
print("All crisis scenarios handled successfully. Archives secure.")

    


   
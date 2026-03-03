import sys
print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

archivist_ID = input("Input Stream active. Enter archivist ID: ")
status = input("Input Stream active. Enter status report: ") 

sys.stdout.write(f"\n[STANDARD] Archive status {archivist_ID}:  {status}\n")
sys.stderr.write("[ALERT] System diagnostic: Communication channels verified\n")
sys.stdout.write("[STANDARD] Data transmission complete\n")
print("\nThree-channel communication test successful.")


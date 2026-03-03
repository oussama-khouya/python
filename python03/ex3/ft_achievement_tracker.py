
alice_ach = set(['first_kill', 'level_10', 'treasure_hunter', 'speed_demon'])
bob_ach  = set(['first_kill', 'level_10', 'boss_slayer', 'collector'])
charlie_ach = set(['level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon','perfectionist'])
all_unique = alice_ach.union(bob_ach,charlie_ach)
total_ach = len(all_unique)
common = alice_ach.intersection(bob_ach,charlie_ach)
rare_ach_p1 = alice_ach.difference(bob_ach,charlie_ach)
rare_ach_p2 = bob_ach.difference(alice_ach,charlie_ach)
rare_ach_p3 = charlie_ach.difference(bob_ach,alice_ach)
rare_ach = rare_ach_p1.union(rare_ach_p2,rare_ach_p3)
print("=== Achievement Tracker System ===\n")
print(f"Player alice achievements: {alice_ach}")
print(f"Player bob achievements: {bob_ach}")
print(f"Player charlie achievements: {charlie_ach}\n")
print("=== Achievement Analytics ===")
print(f"All unique achievements: {all_unique}")
print(f"Total unique achievements: {total_ach}\n")
print(f"Common to all players: {common}")
print(f"Rare achievements (1 player): {rare_ach}\n")
avb = alice_ach.intersection(bob_ach)
aunique = alice_ach.difference(bob_ach)
bunique = bob_ach.difference(alice_ach)
print(f"Alice vs Bob common: {avb}")
print(f"Alice unique: {aunique}")
print(f"Bob unique: {bunique}")







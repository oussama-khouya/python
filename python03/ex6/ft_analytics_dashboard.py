print("=== Game Analytics Dashboard ===\n")
players = ['alice', 'charlie', 'diana', 'bob']
scores =[2800 ,2700 , 2001 ,1800]
active = [True, False,False, True]
regions = ["north", "east", "central", "east","north"]
achievements = {
    "alice":   ["first_kill", "level_10", "boss_slayer", "ghost"],
    "bob":     ["first_kill", "level_10", "jinn"],
    "charlie": ["first_kill", "level_11", "boss","legend", "champion"],
    "diana":   ["first_kill", "level_10", "boss_slayer", "sniper"]
}

print("=== List Comprehension Examples ===")
high_score = [players[i] for i in range(len(players)) if scores[i] > 2000]
print(f"High scorers (>2000): {high_score}")
score_doubled = [i * 2 for i in scores]
print(f"Scores doubled: {score_doubled}")
active_players = [players[i] for i in range(len(players)) if active[i] == True]
print(f"Active players: {active_players}")

print("\n=== Dict Comprehension Examples ===")
dic_player = {players[d] : scores[d] for d in range(len(players))}
print(f"Player scores: {dic_player}\n")

score_cat = {
    "high" : len([s for s in scores if s > 2500])
    ,"meduim" : len([sc for sc in scores if 2000 <= sc <= 2500 ])
    ,"low" : len([sco for sco in scores if sco < 2000])
}
print(f"Score categories: {score_cat}")
Achievement_counts = {pe : len(achievements[pe]) for pe in players}
print(f"Achievement counts: {Achievement_counts}\n")

print("=== Set Comprehension Examples ===")
unique_player = {p for p in players}
print(f"Unique players: {unique_player}")
unique_ach = {ach for p in players for ach in achievements[p] }
print(f"Unique achievements: {unique_ach}")
active_regions = {r for r in regions}
print(f"Active regions: {active_regions}")

print("\n=== Combined Analysis ===")
print(f"Total players: {len(players)}")
print(f"Total unique achievements: {len(unique_ach)}")
averge = sum (scores)/ len (scores)
print(f"Average score: {averge:.1f}")

top = players[0]
top_score = scores[0]
for i in range(len(players)):
    if scores[i] > top_score:
        top_score = scores[i]
        top = players[i]
print(f"Top performer: {top} ({top_score} points, {len(achievements[top])} achievements)")
















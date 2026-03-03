import sys
print("=== Player Score Analytics ===")
lenn = len(sys.argv)
if lenn > 1:
    score = [] #list.append()
    for argv in sys.argv[1:]:
        try:
            score.append(int(argv))
        except ValueError:
            print(f"Invalid score: {argv}")
    print(f"Scores processed: {score}")
    print(f"Total players: {len(score)}")
    print(f"Total score: {sum(score)}")
    print(f"Average score: {sum(score) / len(score)}")
    print(f"High score: {max(score)}")
    print(f"Low score: {min(score)}")
    print(f"Score range: {max(score) - min(score)}")
else:
    print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")






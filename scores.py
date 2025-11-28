import sys

if len(sys.argv) > 1:
    scores = list(map(int, sys.argv[1:]))
    print("User provided scores:")
else:
    
    scores = [50, 60, 70, 80, 90]
    print("No input given - using default scores:")


total = sum(scores)
average = total / len(scores)



print(f"Scores: {scores}")
print(f"Sum of scores: {total}")
print(f"Average of scores: {average:.2f}")

  

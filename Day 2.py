points = 0

file = open("Inputs/input2", 'r')
points_dict = {"A X": 4,
          "A Y": 8,
          "A Z": 3,
          "B X": 1,
          "B Y": 5,
          "B Z": 9,
          "C X": 7,
          "C Y": 2,
          "C Z": 6,
         }

for line in file:
    points += points_dict[line.strip()]
print(points)
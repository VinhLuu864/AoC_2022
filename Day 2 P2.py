points = 0

file2 = open("Inputs/input2", 'r')
#Rock 1 Paper 2 Scissors 3
#X Lose, Y Draw, Z Win
points_dict = {"A X": 3+0,   #Rock, Lose = Scissors
          "A Y": 1+3, #Rock, Draw = Rock
          "A Z": 2+6, #Rock, Win = Paper
          "B X": 1+0, #Paper, Lose = Rock
          "B Y": 2+3, #Paper, Draw = Paper
          "B Z": 3+6, #Paper, Win = Scissors
          "C X": 2+0, #Scissors, Lose = Paper
          "C Y": 3+3, #Scissors, Draw = Scissors
          "C Z": 1+6, #Scissors, Win = Rock
         }

for line in file2:
    points += points_dict[line.strip()]
print(points)
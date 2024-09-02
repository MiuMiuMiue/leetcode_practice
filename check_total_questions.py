import os

difficulty = "easy"
num = 0

for file in os.listdir(os.getcwd()):
    if difficulty in file:
        num += 1

print(f"{num} {difficulty} questions finished.")
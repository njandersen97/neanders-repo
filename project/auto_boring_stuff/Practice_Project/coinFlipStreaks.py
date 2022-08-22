import random

random.seed(1)

numberOfStreaks = 0
total_streaks = 0

for experimentNumber in range(10000):
    #Code that creates a list of 100 'heads' or 'tails' values.
    flips = []
    for _ in range(100):
        if random.randint(0, 1) == 1:
            flips.append('H')
        else:
            flips.append('T')
    #Code that checks if there is a streak of 6 heads or tails in a row.
    current_streak = 1
    previous_flip = None
    for flip in flips:
        if flip == previous_flip:
            current_streak += 1
            if current_streak == 6:
                total_streaks += 1
                break
        else:
            current_streak = 1
        previous_flip = flip
percentage_with_streaks = total_streaks / 10000
print(
    f'Percentage of runs with a streak of 6: '
    f'{percentage_with_streaks*100:.2f}%'
)
import csv
import time

directions = []
values = []

aim = 0 
backup_aim = 1
depth = 0
distance = 0
total = 0
with open('day2.csv', 'r') as file:
    reader = csv.reader(file)
    for lines in reader:
        x, y = lines[0].split()
        directions.append(x)
        values.append(int(y))

for i in range(len(directions)):
    if directions[i] == 'forward':
        distance += values[i]
        depth += aim * values[i] 

    elif directions[i] == 'up':
        aim -= values[i]
        continue
    elif directions[i] == 'down':
        aim += values[i]
        continue

    else:
        print('direction detection error')
    

answer = distance * depth
print(answer)



start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))

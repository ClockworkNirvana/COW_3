import csv

lines = []
with open("toxyz.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    y = 130
    for row in reader:
        x = -80
        for data in row:
            lines.append('{} {} {}'.format(x, y, data))
            x += 1
        y -= 1

with open('mesh.xyz', 'x') as f:
    for line in lines:
        f.write(line)
        f.write('\n')

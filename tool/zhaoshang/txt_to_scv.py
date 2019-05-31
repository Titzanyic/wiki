import csv
import sys
file = open(str(sys.argv[1]), "r")
out_put_csv = str(sys.argv[2])
lines = file.readlines()
count = len(lines)
print(count)
list = []
for i in range(count):
    if i % 8 == 0:
        line = {'jyr': lines[i].replace('\n', ''), 'jsr': lines[i + 1].replace('\n', ''),
                'jyzh': lines[i + 2].replace('\n', ''), 'rmb': lines[i + 3].replace('\n', ''),
                'kh': lines[i + 4].replace('\n', ''),
                'type': lines[i + 5].replace('\n', ''), 'jyje': lines[i + 6].replace('\n', '')}
        list.append(line)

with open(out_put_csv, 'w') as csvfile:
    fieldnames = ['jyr', 'jsr', 'jyzh', 'rmb', 'kh', 'type', 'jyje']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for zh in list:
        writer.writerow(zh)
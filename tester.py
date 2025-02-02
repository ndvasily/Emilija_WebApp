import csv

filepath='ml_log.txxxxt'
with open(filepath , 'r') as file:
    ml_logd = list(csv.reader(file, delimiter=","))    # mnogu poprofi e vaka

print(ml_logd)

for l in ml_logd:
    print(l)
    for s in l:
        print(s)

#  [['23:53:00', ' 100', ' Mama', ' 2025-02-01']]
#  [['23:53:00', ' 100', ' Mama', ' 2025-02-01'], '23:53:00, 200, Formula, 2025-02-01\n']

with open(filepath , 'w', newline='') as file:
    csv.writer(file, delimiter=" ")    # mnogu poprofi e vaka

def write_ml_log(ml_arg, filepath='ml_log.txt'):
    with open(filepath, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(ml_arg)
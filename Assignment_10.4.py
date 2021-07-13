name = input("Enter file name:")
handle = open(name)

all_hours = list()
for line in handle :
    if not line.startswith('From ') : continue
    else :
        line = line.split()
        time = line[5].split(':')
        all_hours.append(time[0])

hm_hours = dict()
for hour in all_hours :
        hm_hours[hour] = hm_hours.get(hour, 0) + 1

total_hours = hm_hours.items()
for k, v in sorted(total_hours) :
    print(k, v)

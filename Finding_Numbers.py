import re
handler = open('regex_sum_1075212.txt')

total_sum = 0
for line in handler :
    line = line.rstrip()
    line_list = re.findall('[0-9]+', line)
    for number in line_list :
        a = int(number)
        total_sum += a
print(total_sum)

name = input("Enter file: ")
holder = open(name)

mail_addresses = dict()
biggest_times = None
biggest_email = None

for line in holder :
    if not line.startswith('From ') : continue
    else :
        line = line.split()
        email = line[1]
        mail_addresses[email] = mail_addresses.get(email, 0) + 1

for email,times in mail_addresses.items() :
    if biggest_times is None or times > biggest_times :
        biggest_times = times
        biggest_email = email
print(biggest_email, biggest_times)

fname = input("Enter file name: ")
fh = open(fname)

contador = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    contador += 1
    p = line.find(':')
    numero = line[p+1:]
    suma_numero += float(numero)

average = (suma_numero/contador)
print("Average spam confidence:", total)








# Write a program that prompts for a file name, then opens that file and reads
# through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines
# and compute the average of those values and produce an output as shown below.
# Do not use the sum() function or a variable named sum in your solution.

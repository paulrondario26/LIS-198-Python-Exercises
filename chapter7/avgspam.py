c = 0
t = 0

file = input("Please enter the file name: ")
fhandle = open(fname)

for line in fhandle:
    if line.startswith("X-DSPAM-Confidence: "):
        c = c + 1
        position = line.find(":")
        number = line[position+1:].strip()
        tspam = float(number)
        total = total + tspam

a = t / c
print(a)

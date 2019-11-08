c = 0
file = input('Enter the file name: ')


if file == "na na boo boo":
	print("na na boo hoo")
else: fhandle = open(file)
for line in fhandle:
    if line.startswith("X-DSPAM-Confidence: "):
        c = c + 1
        position = line.find(":")
        number = line[position+1:].strip()
        tspam = float(number)
        total = total + tspam

a = t / c
print(a)

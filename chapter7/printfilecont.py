file = input("Enter a file name:")
fhandle = open(file)
for line in fhandle:
    line = line.upper()
    print(line)

list = []
fhandle = open("romeo.txt")
for line in fhandle:
    words = line.split()
    for word in words:
        if word in list:
        list.append(word)
print(list)

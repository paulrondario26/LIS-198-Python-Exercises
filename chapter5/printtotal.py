t = 0
c = 0

while True:
    userinp = input("Please enter your number!: ")
    if userinp == "Done":
        break

    elif userinp != "Done":
        userinp = float(userinp)
        t = t + float(userinp)
        c = c + 1

print (t, c, t/c)

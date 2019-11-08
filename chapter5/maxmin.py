t = 0
c = 0
max = 0
min = 0
while True:
    userinp = input("Please enter your number!: ")
    if userinp == "Done":
        break

    elif userinp != "Done":
        userinp = float(userinp)
        t = t + float(userinp)
        c = c + 1
        if max == 0 and min == 0:
            max = userinp
            min = userinp
        elif userinp > max:
            max = userinp
        elif userinp < min:
            min = userinp


print(t, c, max, min)

phrs = input("Hours: ")
prt = input("Rate: ")
if float(phrs) > 40:
    ppy = ((float(phrs) - 40)) * (1.5 * (float(prt))) + (40 * float(prt))
print("Pay: ", ppy)

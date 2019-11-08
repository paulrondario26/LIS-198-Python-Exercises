grade = input("Enter Score between 0.0 and 1.0: ")
try:
    grade = float(grade)
except:
    print("Please Enter a numerical value")
    exit()

if grade >1.0:
    print("Please Enter a numerical value between 0.0 and 1.0.")
elif grade >= 0.9 and grade <1.0:
    print("A")
elif grade <0.9 and grade >= 0.8:
    print("B")
elif grade <0.8 and grade >= 0.7:
    print("C")
elif grade <0.7 and grade >= 0.6:
    print("D")
else: print("F")

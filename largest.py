a = int(input ("enter a first num: "))
b = int(input("enter a second num: "))
c = int(input("enter a third num: "))

largest = a if (a>b and b>c) else (b if b>c else c)

print("the lagrest number is:", largest)
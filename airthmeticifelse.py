first = input("enter frist num:")
operator = input ("enter operator (+,-,*,/,%) :")
second = input("enter second num:")
first = int(first)
second = int(second)

if operator == "+":
    print (first + second)
elif operator == "-":
    print (first - second)
elif operator == "*":
    print (first * second)
elif operator == "/":
    print (first / second)
elif operator == "%":
    print (first % second)
else:
    print(invalid)
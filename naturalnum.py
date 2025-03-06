N = int(input("enter the nth term to find out the natural number"))
if N > 0:
    totalsum = sum(range(1, N + 1))
    # print(f"sum of first {N} natural number is: {totalsum}")
    print("The sum of first", N,"natural number is:", totalsum)
else:
    print("invalid")
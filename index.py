m = float(input("Input M\n"))
n = float(input("Input N\n"))
fraction = m/n
for i in range(50): print("-", end ="")
print("\nFraction is " + str(round(fraction, 3)))
for i in range(50): print("-", end ="")
bigger = int(fraction)%10
smaller = int((fraction - int(fraction))*10)
if fraction==int(fraction):
    print("\nThe younger figure of the whole part is " + str(bigger) + ".")
    print("\nWe cannot define the older part of the fractional part, because a fraction is an integer.\n")
else:
    print("\nThe younger figure of the whole part is " + str(bigger) + ".")
    print("\nThe older part of the fractional part is " + str(smaller) + ".\n")
temp = float(input()) #чтобы консоль не закрывалась

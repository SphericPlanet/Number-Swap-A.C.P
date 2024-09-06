x=int(input("Enter the digit of x: "))
y=int(input("Enter the digit of y: "))
z=int(input("Enter the digit of z: "))

print("Value of X before it got swaped",x)
print("Value of Y before it got swaped",y)
print("Value of Z before it got swaped",z)

temp = x
x = y
y = z
z = temp


print("Value of X after swapping",x)
print("Value of Y after swaping",y)
print("Value of Z after swaping",z)
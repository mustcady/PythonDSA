x,y,z=input().split()
x=int(x)
y=int(y)
z=int(z)
if (x>y) and (x>z):
    largest=x
elif (y>x) and (y>z):
    largest=y
else:
    largest=z
print(largest)
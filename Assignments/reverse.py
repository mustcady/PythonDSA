n=int(input())
rev=0
remain=0
while n!=0:
    remain=n%10
    rev=rev*10+remain
    n=n//10
print(rev)
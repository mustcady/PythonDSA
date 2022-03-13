num=int(input())
d=int(input())
count=0
while num!=0:
    if num%10==d:
        count+=1
    num=num//10
print(count)
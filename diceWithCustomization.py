# With inbuilt  random packages
import random as r
a=r.randint(1,6)    # it selects a random number between the lower and upper limit,including them both
b=r.choice([2,4,6]) # it selects a number from the given sequence
c=r.choice([1,3,5]) 
print("The dice roll using random module. It is an unbiased dice : ",a)
print("The dice roll using random module. It is an even biased dice : ",b)
print("The dice roll using random module. It is an odd biased dice : ",c)

print("*****************************************************************")
# without inbuilt random packages
import datetime as dt
x=str(dt.datetime.now())
d=x[-1]
d=int(d)
if d==0:
    d=1
#print(d)
if d<=6:
    print("The dice roll without using random module. It is unbiased : ",d)
if d>=7:
    print("The dice roll without using random module. It is unbiased : ",d-6)

if d%2==0:
    e=d+1
else:
    if d==9:
        e=d-1
    else:
        e=d+1


if d in [1,3,5,7,9]:
    if d<=6:
        print("The dice roll without using random module. It is an odd biased dice : ",d)
    if d>=7:
        print("The dice roll without using random module. It is an odd biased dice : ",d-6)    


if d in [2,4,6,8]:
    if d<=6:
        print("The dice roll without using random module. It is an even biased dice : ",d)
    if d>=7:
        print("The dice roll without using random module. It is an even biased dice : ",d-6)  

if e in [1,3,5,7,9]:
    if e<=6:
        print("The dice roll without using random module. It is an odd biased dice : ",e)
    if e>=7:
        print("The dice roll without using random module. It is an odd biased dice : ",e-6)    


if e in [2,4,6,8]:
    if e<=6:
        print("The dice roll without using random module. It is an even biased dice : ",e)
    if e>=7:
        print("The dice roll without using random module. It is an even biased dice : ",e-6)  
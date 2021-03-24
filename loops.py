a,b=0,1
num=int(input("enter your maximum value :"))

while a<num:
    print(a)
    a,b=b,a+b

x=int(input("enter a number"))
if x<0:
    x=0
    print("negative changed to zero")
elif x==1:
    print("single")
else:
    print("more")

words=['cat','dog','chicken','horse']
for a in words:
    print(a,len(a))

for a in words[:]:
    if len(a)>6:
        words.insert(0,a)
        print(words)

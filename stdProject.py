import math,csv 
with open("stdData.csv",newline="") as f:
    r=csv.reader(f)
    data=list(r)
file=data[0]
total=0

for x in file:
    total+=int(x)

mean=total/len(file)
squaredList=[]
for n in file:
    a=int(n)-mean
    a=a**2
    squaredList.append(a)
sum=0
for i in squaredList:
    sum+=i
res=sum/(len(file)-1)
sd = math.sqrt(res)    
print("Standard Deviation = ")
print(sd)
#print("                        ")
print("Mean= ")
print(mean)

     
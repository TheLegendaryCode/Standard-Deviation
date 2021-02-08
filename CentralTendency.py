"""Mean , median, mode"""
import csv
with open("SOCR-HeightWeight.csv",newline="") as f:
    r=csv.reader(f)
    data=list(r)
data.pop(0)
newData=[]
for i in range(len(data)):
    n=data[i][1]
    newData.append(float(n))
num=len(newData)
"""total=0
print(newData)
for x in newData:
    total+=x
mean=total/num
print(mean)"""
newData.sort()
if num%2==0:
    m1=float(newData[num//2])
    m2=float(newData[num//2-1])
    median=(m1+m2)/2
else :
    median=newData[num//2]
print(median)
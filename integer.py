numlist1=[]
numlist2=[]
sum1=0
sum2=0
n1=int(input("Enter the Number of Digit To be Inserted in List 1:"))
for i in range(n1):
    print("Digit",i+1,end=":")
    numlist1.append(int(input()))
n2=int(input("Enter the Number of Digit To be Inserted in List 2:"))
for i in range(n2):
    print("Digit",i+1,end=":")
    numlist2.append(int(input()))
for i in numlist1:
    sum1=sum1+i
for i in numlist2:
    sum2=sum2+i
if sum1 == sum2:
    print("!!! Sum of 2 list is the Same !!!")
else:
    print("!!! Sum of 2 list is not the Same !!!")

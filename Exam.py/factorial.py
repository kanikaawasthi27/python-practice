import math
# with function
num = int(input("enter a number:"))
fact = math.factorial(num)
print("factorial is:", fact)
#without function
flag = 1
for i in range(1,num+1):
    flag = flag*i
print ("factorial without function is:", flag)    
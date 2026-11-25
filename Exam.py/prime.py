num = int(input("enter a number:"))
count = 0
for i in range(2,num):
    if num%i == 0:
        count = count + 1
        break
if count > 0 or num <= 1 :
    print("number is not prime")
else:
    print("number is prime")  
          

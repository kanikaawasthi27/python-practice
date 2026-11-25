num = int(input("enter a number:"))
total = 0
for i in range(len(str(num))):
    rem = num%10
    total = total + rem
    num = num // 10
print("sum of digits:", total)    

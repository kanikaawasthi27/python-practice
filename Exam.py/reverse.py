num = int(input("enter a number:"))
rev = 0
temp = num
for i in range(len(str(num))):
    rem = num%10
    rev = rev * 10 + rem
    num = num // 10
print("reverse number is:", rev)    
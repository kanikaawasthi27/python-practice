num = int(input("enter a number:"))
rev = 0
tem = num
for i in range(len(str(num))):
    rem = num%10
    rev = rev*10 + rem
    num = num // 10
if tem == rev:
    print("palindrome") 
else:
    print("not palindrome")

    
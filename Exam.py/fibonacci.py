# withoput function
num = int(input("enter terms:"))
a = 0
b = 1
for i in range(num):
    print(a, end =" ")
    c = a+b
    a = b
    b = c
print()    
# with function
#n = int(input("enter terms:"))
def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a, end = " ")
        c = a+b
        a = b
        b = c
print("fibonacci series is:")
fibonacci(num)            
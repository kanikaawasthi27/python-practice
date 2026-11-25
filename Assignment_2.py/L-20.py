lis = list(map(int , input("enter a list:").split()))
len = 0
for i in lis:
    len = len + 1
print(lis[:(len-1)])
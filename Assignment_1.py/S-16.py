s1 = input("enter first string:")
s2 = input("enter second string:")
len1 = 0
len2 = 0
result = 0
for i in s1:
    len1 +=1
for i in s2:
    len2 +=1
if len1 == len2:   
    for i in s1 :
        if i not in s2:
            result = False
            break
        else :
            result = True
if result == True:
    print("strings are anagram")
else:
    print("string are not anagram")    
            

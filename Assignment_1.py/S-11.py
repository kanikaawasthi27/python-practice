s = "kanaika"
ch = "a"
len = 0
for i in s:
    len += 1
index = len -1    
for i in s:
    if ch != i:
        count +=1
        for i in (0,index):
            print(s[i])
            break
        
dit = {1:87,2:90,3:91,4:95,5:85}
given = 6
flag = 0
for i in dit:
    if i == given:
        flag = flag +1
        break
if flag == 1:
    print("key is exist")
else:
    print("key is not exist")        
        
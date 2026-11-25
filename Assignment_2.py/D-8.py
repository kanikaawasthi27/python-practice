dit = {1:87,2:90,3:91,4:95,5:85}
given = 90
flag = 0
for val in dit.values():
    if val == given:
        flag = flag +1
        break
if flag == 1:
    print("value is exist")
else:
    print("value is not exist")        
dit = {"siya":90,"luv":99,"kanika":86,"harshit":89}
max = dit["siya"]
for i in dit:
    if max < dit[i]:
        max = dit[i]
print("largest value is:", max)        
s = "kanikaawasthi143@gmail.com"
alph = 0
digi = 0
sep_char = 0
digit = "0123456789"
for i in s:
    if "a"<=i>="z" or "A"<=i>="Z":
        alph +=1
    elif i in digit:
        digi +=1 
    else:
        sep_char +=1
          
print(alph)
print(digi)
print(sep_char)
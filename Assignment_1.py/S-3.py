s = "Python is easy and powerfull language"
vowels = "aeiouAEIOU"
count = 0
for i in s:
    if (i not in vowels and i != " "):
        count +=1
print(" numbers of consonants is:",count)        
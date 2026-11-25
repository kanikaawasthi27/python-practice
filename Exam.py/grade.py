math = float(input("enter maths marks:"))
sci = float(input("enter science marks:"))
eng = float(input("enter english marks:"))
com = float(input("enter computer marks:"))
hindi = float(input("enter hindi marks:"))
total = math+sci+eng+com+hindi
print("total marks:", total)
per = (total/500) * 100
print("percentage is:", per)
if per >= 90:
    print("grade: A+")
elif  per >= 75:
    print("grade: A")
elif  per >= 60:
    print("grade: B")
elif  per >= 45:
    print("grade: C")
else:
    print("fail")  
def sim_intrest(p,r,t):
    SI = (p*r*t)/100
    return SI
def com_intrest(p,r,t):
    A = p* (1 + r/100)**t
    CI = A - p
    return CI
p = int(input("enter principle ammount:"))
r = int(input("rate of intrest:"))
t = int(input("enter year"))
print("simple intrest is:",sim_intrest(p,r,t))
print("compound intrest is:", com_intrest(p,r,t))

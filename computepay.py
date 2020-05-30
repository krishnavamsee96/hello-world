# KRISHNA VAMSEE DUGGARAJU
# 800688160
h=int(input("Enter hours:"))
p=int(input("Enter pay:"))
def computepay(h,p):
    if h>40 :
        grosspay = (40*p)+ (h-40)*p*1.5
    elif h<=40 :
        grosspay = (h*p)
    return grosspay
pay = computepay(h,p)
print("gross pay is:",pay)

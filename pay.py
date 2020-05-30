# KRISHNA VAMSEE DUGGRAJU
# 800688160
h = int(input("Enter no of working hours:"))
p = int(input("Enter the rate per hour:"))
if h>40 :
    pay = 40*p
    extra = (h-40)*p*1.5
    ot = float(extra)
    grosspay = pay+ot
elif h<=40 :
    grosspay = h*p
print("grosspay for the month is:", grosspay)

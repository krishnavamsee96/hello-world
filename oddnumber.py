a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
c = int(input("Enter the value of c:"))

if a%2 == 0 and b%2 == 0 and c%2 == 0 :
	print("All are Even numbers")
elif a%2 != 0 and b%2 == 0 and c%2 == 0 :
	print("a is the greatest odd number")
elif a%2 == 0 and b%2 != 0 and c%2 == 0 :
	print("b is the greatest odd number")
elif a%2 == 0 and b%2 == 0 and c%2 != 0 :
	print("c is the greatest odd number")
elif a%2 == 0 and b%2 !=0 and c%2 !=0 :
	if b>c :
		print("b is the greatest odd number")
	else :
		print("c is the greatest odd number")
elif a%2 != 0 and b%2 != 0 and c%2 == 0 :
	if a>b :
		print("a is the greatest odd number")
	else :
		print("b is the greatest odd number")
elif a%2 != 0 and b%2 == 0 and c%2 != 0 :
	if a>c :
		print("a is the greatest odd number")
	else :
		print("c is the greatest odd number")
elif a%2 != 0 and b%2 != 0 and c%2 != 0 :
	if a>b and a>c :
		print("a is the greatest odd number")
	if b>c :
		print("b is the greatest odd number")
	else :
		print("c is the greatest odd number")

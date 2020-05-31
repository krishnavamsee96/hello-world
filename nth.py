n = int(input("Enter the value of n:"))

def triangular_series(n):
	b = 1 
	c = 1
	for a in range (1, n+1):
		print(c, end = ' ')
		b = b+1
		c = c+b
	
	for a in range (1,n+1):
		print(a*(a+1)/2, end = ' ')
		
triangular_series(n)

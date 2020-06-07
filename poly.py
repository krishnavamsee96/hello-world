# Krishna Vamsee Duggaraju
# 800688160
# Let a4 = 10, a3 = 5, a2 = 8, a1 = 1, a0 = 9
# Let the polinomial is 10x^4+5x^3+8x^2+x+9 at x=5
poly = [10, 5, 8, 1, 9]
x = 5
n = len(poly)
def polynomial(poly, n, x):
	evl = poly[0]
	for i in range(1,n):
		evl = evl*x + poly[i]
	return evl
print("value of polynomial is ", polynomial(poly, n, x))
# Evaluated answer is 7089

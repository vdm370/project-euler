def gcd(a, b):
	if b == 0:
		return a
	return gcd(b, a % b)

def lcm(a, b):
	return a // gcd(a, b) * b

lc = 1
for i in range(2, 21):
	lc = lcm(lc, i)
print(lc)

for a in range(1, 1001):
	for b in range(1, 1001):
		c = 1000 - a - b
		if c < 1 or c > 1000:
			continue
		if a * a + b * b == c * c:
			print(a, b, c, a * b * c)
			exit()

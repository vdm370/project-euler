ans = 0
for i in range(100, 1000):
	for j in range(100, 1000):
		x = i * j
		x_s = str(x)
		if x_s == x_s[::-1]:
			ans = max(ans, i * j)
print(ans)

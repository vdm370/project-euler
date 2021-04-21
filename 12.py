def div_cnt(x):
	cnt = 1
	i = 2
	while i * i <= x:
		mini_cnt = 0
		while x % i == 0:
			mini_cnt += 1
			x //= i
		cnt *= mini_cnt + 1
		i += 1
	if x > 1:
		cnt *= 2
	return cnt

n = 1
while True:
	t = n * (n + 1) // 2
	if div_cnt(t) > 500:
		print(t)
		exit()
	n += 1
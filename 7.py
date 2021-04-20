def prime(x):
	i = 2
	while i * i <= x:
		if x % i == 0:
			return False
		i += 1
	return True

need = 10001
i = 2
while need > 0:
	if prime(i):
		need -= 1
	i += 1
print(i - 1)

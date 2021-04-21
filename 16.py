def sum_dig(x):
	if x == 0:
		return 0
	return x % 10 + sum_dig(x // 10)

print(sum_dig(2 ** 1000))

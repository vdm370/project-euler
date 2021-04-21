from num2words import num2words
ans = 0
for i in range(1, 1001):
	s = num2words(i)
	for c in s:
		if c.isalnum():
			ans += 1
print(ans)
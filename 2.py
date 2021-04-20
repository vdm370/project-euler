f = 0
s = 1
ans = 0
while True:
	n = f + s
	if n > 4000000:
		break
	if n % 2 == 0:
		ans += n
	f = s
	s = n
print(ans)

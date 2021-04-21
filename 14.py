def f(x):
	if x % 2 == 0:
		return x // 2
	return 3 * x + 1

mp = {}

def len(x):
	if x == 1:
		return 0
	global mp
	if x in mp:
		return mp[x]
	mp[x] = 1 + len(f(x))
	return mp[x]

ans, num = 0, -1
for i in range(1, 1000001):
	if len(i) > ans:
		ans = len(i)
		num = i

print(ans, num)

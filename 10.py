def prime(x):
        i = 2
        while i * i <= x:
                if x % i == 0:
                        return False
                i += 1
        return True

ans = 2
for i in range(3, 2000000, 2):
	if prime(i):
		ans += i
print(ans)

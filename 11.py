n = 20
mat = [[] for i in range(n)]
for i in range(n):
	line = input()
	mat[i] = list(map(int, line.split()))
dx = [0, 1, 0, -1, 1, 1, -1, -1]
dy = [1, 0, -1, 0, 1, -1, 1, -1]

def valid(n, i, j):
	return i >= 0 and i < n and j >= 0 and j < n

ans = 0
for i in range(n):
	for j in range(n):
		for d in range(8):
			if valid(n, i + 3 * dx[d], j + 3 * dy[d]):
				cur = 1
				for k in range(4):
					cur *= mat[i + k * dx[d]][j + k * dy[d]]
				ans = max(ans, cur)

print(ans)
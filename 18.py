n = 15
mat = [[] for i in range(n)]
for i in range(n):
	mat[i] = list(map(int, input().split()))

INF = 99999999999999999999
dp = [[-INF for i in range(n)] for j in range(n)]
dp[0][0] = mat[0][0]
for i in range(1, n):
	dp[i][0] = dp[i - 1][0] + mat[i][0]
	dp[i][i] = dp[i - 1][i - 1] + mat[i][i]
	for j in range(1, i):
		dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + mat[i][j]

print(max(dp[n - 1]))

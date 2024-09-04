import sys

input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

dp[0][0] = board[0][0]

for r in range(1, n):
    dp[r][0] = dp[r - 1][0] + board[r][0]

for c in range(1, n):
    dp[0][c] = dp[0][c - 1] + board[0][c]

for r in range(1, n):
    for c in range(1, n):
        dp[r][c] = max(dp[r][c - 1] + board[r][c], dp[r - 1][c] + dp[r][c])
    
result = 0
for c in range(n):
    result = max(result, dp[n - 1][c])

print(result)
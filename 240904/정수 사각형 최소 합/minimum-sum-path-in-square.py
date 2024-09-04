import sys

input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

dp[0][n - 1] = board[0][n - 1]

for r in range(1, n):
    dp[r][n - 1] = dp[r - 1][n - 1] + board[r][n - 1]

for c in range(n - 2, -1, -1):
    dp[0][c] = dp[0][c + 1] + board[0][c]

for r in range(1, n):
    for c in range(n - 2, -1, -1):
        dp[r][c] = min(dp[r - 1][c], dp[r][c + 1]) + board[r][c]

print(dp[n - 1][0])
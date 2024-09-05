import sys

input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[1] * n for _ in range(n)]

cells = []
result = 0

for i in range(n):
    for j in range(n):
        cells.append((board[i][j], i, j))

cells.sort()

for _, r, c in cells:
    drs, dcs = [-1, 1, 0, 0], [0, 0, -1, 1]

    for dr, dc in zip(drs, dcs):
        nr, nc = r + dr, c + dc
        if 0 < nr < n and 0 <= nc < n and board[nr][nc] > board[r][c]:
            dp[nr][nc] = max(dp[nr][nc], dp[r][c] + 1)

for r in range(n):
    for c in range(n):
        result = max(result, dp[r][c])

print(result)
import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * (n + 4)
dp[1] = 0
dp[2] = 1
dp[3] = 1
dp[4] = 1

for i in range(5, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n])
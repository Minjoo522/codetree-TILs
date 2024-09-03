import sys

input = sys.stdin.readline

n = int(input())
dp = [0] * 1000
dp[0] = 1  # 아예 놓지 않는 경우
dp[1] = 1

for i in range(2, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 10007

print(dp[n])
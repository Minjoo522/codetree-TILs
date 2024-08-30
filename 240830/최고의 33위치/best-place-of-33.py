import sys

input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

def find_money(r, c, last_r, last_c):
    cnt = 0
    for nr in range(r, last_r + 1):
        for nc in range(c, last_c + 1):
            if board[nr][nc] == 1:
                cnt += 1
    return cnt

result = 0
for r in range(N):
    for c in range(N):
        if r + 2 >= N or c + 2 >= N:
            continue
        else:
            result = max(result, find_money(r, c, r + 2, c + 2))

print(result)
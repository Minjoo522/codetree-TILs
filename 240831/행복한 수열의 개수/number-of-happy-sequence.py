import sys
from collections import defaultdict

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

cnt = 0

def find_happy_sequence_row(r):
    current_num = 0
    cnt = 0
    for i in range(n):
        if current_num == board[r][i]:
            cnt += 1
        else:
            current_num = board[r][i]
            cnt = 1
        if cnt >= m:
            return True
    return False

def find_happy_sequence_column(c):
    current_num = 0
    cnt = 0
    for i in range(n):
        if current_num == board[i][c]:
            cnt += 1
        else:
            current_num = board[i][c]
            cnt = 1
        if cnt >= m:
            return True
    return False

for i in range(n):
    if find_happy_sequence_row(i):
        cnt += 1
    if find_happy_sequence_column(i):
        cnt += 1

print(cnt)
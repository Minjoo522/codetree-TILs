import sys

input = sys.stdin.readline

def get_gold_sum(r, c, K):
    return sum([
        board[i][j]
        for i in range(n)
        for j in range(n)
        if abs(r - i) + abs(c - j) <= K
    ])

def get_area(K):
    return K * K + (K + 1) * (K + 1)

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

max_gold_count = 0

for r in range(n):
    for c in range(n):
        for K in range(2 * (n - 1) + 1):
            gold_count = get_gold_sum(r, c, K)
            if gold_count * m >= get_area(K):
                max_gold_count = max(max_gold_count, gold_count)

print(max_gold_count)
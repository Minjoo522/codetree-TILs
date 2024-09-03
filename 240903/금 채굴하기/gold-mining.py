import sys

input = sys.stdin.readline

def get_gold_in_border(r, c, K):
    drs = [1, 1, -1, -1]
    dcs = [-1, 1, 1, -1]

    if K == 0:
        return board[r][c]

    gold_sum = 0
    curr_r, curr_c = r - K, c
    for dr, dc in zip(drs, dcs):
        for step in range(K):
            if 0 <= curr_r < n and 0 <= curr_c < n:
                gold_sum += board[curr_r][curr_c]
            
            curr_r, curr_c = curr_r + dr, curr_c + dc
    
    return gold_sum

def get_area(K):
    return K * K + (K + 1) * (K + 1)

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

max_gold_count = 0

for r in range(n):
    for c in range(n):
        gold_count = 0
        for K in range(2 * (n - 1) + 1):
            gold_count += get_gold_in_border(r, c, K)

            if gold_count * m >= get_area(K):
                max_gold_count = max(max_gold_count, gold_count)

print(max_gold_count)
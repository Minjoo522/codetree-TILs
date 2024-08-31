import sys

input = sys.stdin.readline

def get_gold_sum(r, c, K):
    total_gold = 0

    for dr in range(-K, K + 1):
        dc_range = K - abs(dr)
        for dc in range(-dc_range, dc_range + 1):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                total_gold += board[nr][nc]
    
    return total_gold

def calculate_max_gold():
    max_gold_count = 0

    for K in range(n + 1):
        cost = K * K + (K + 1) * (K + 1)
        for r in range(n):
            for c in range(n):
                gold_count = get_gold_sum(r, c, K)
                if gold_count * m >= cost:
                    max_gold_count = max(max_gold_count, gold_count)

    return max_gold_count

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

print(calculate_max_gold())
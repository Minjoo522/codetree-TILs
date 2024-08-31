"""
n * m
블럭이 놓인 칸 안에 적힌 숫자의 합이 최대가 될 때의 결과를 출력
회전하거나 뒤집을 수 있다.

block : [(0, 0), (-1, 0), (0, 1)], [(0, 0), (0, -1), (1, 0)], [(0, 0), (0, -1), (-1, 0)], 
[(0, 0), (0, 1), (0, 2)], [(0, 0), (1, 0), (2, 0)]
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
blocks = [
    [(0, 0), (-1, 0), (0, 1)],  # ㄴ자 기본
    [(0, 0), (0, -1), (1, 0)],  # ㄴ자 시계 방향 90도 회전
    [(0, 0), (0, -1), (-1, 0)], # ㄴ자 반전
    [(0, 0), (1, 0), (0, 1)],   # ㄴ자 시계 방향 180도 회전
    [(0, 0), (0, 1), (0, 2)],   # ㅡ자 기본
    [(0, 0), (1, 0), (2, 0)]    # ㅡ자 90도 회전
]

result = 0

def calculate_block_sum(r, c):
    max_block_sum = 0

    for block in blocks:
        block_sum = 0
        for i in range(3):
            nr, nc = r + block[i][0], c + block[i][1]
            if 0 <= nr < n and 0 <= nc < m:
                block_sum += board[nr][nc]
            else:
                block_sum = 0
                break
        max_block_sum = max(max_block_sum, block_sum)
    return max_block_sum

for r in range(n):
    for c in range(m):
        result = max(result, calculate_block_sum(r, c))

print(result)
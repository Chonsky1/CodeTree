n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
max_cnt = 0

for row in range(0,n-2):
    for col in range(0,n-2):
        cnt = 0
        for i in range(0,3):
            for j in range(0,3):
                if grid[row+i][col+j] == 1:
                    cnt += 1
            max_cnt = max(max_cnt, cnt)

print(max_cnt)
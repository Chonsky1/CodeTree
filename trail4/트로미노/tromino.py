n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

max_res = 0
def block(row,col):
    global max_res
    Sum = 0
    if 0 <= row < n-1 and 0 <= col < m-1:
        for r in range(2):
            for c in range(2):
                Sum += grid[row+r][col+c]
        diry = [0,0,1,1]
        dirx = [0,1,0,1]
        for i in range(4):
            max_res = max(max_res, Sum-grid[row+diry[i]][col+dirx[i]])
    
def line(row,col):
    global max_res
    Sumy = 0
    Sumx = 0
    if 0 <= row < n-2:
        for i in range(3):
            Sumy += grid[row+i][col]
    if 0 <= col < m-2:
        for i in range(3):
            Sumx += grid[row][col+i]
    max_res = max(Sumy, Sumx, max_res)

for row in range(n):
    for col in range(m):
        block(row,col)
        line(row,col)

print(max_res)


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def is_happy(seq):
    cnt = 1
    if cnt >= m:    
        return True
    for i in range(1, len(seq)):
        if seq[i] == seq[i-1]:
            cnt += 1
        else:
            cnt = 1
        if cnt >= m:
            return True
    return False

happy = 0
for i in range(n):
    if is_happy(grid[i]):                           
        happy += 1
    if is_happy([grid[r][i] for r in range(n)]):        
        happy += 1

print(happy)
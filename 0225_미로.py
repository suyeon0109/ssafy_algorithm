def maze():
    while Q:
        I,J = Q.pop(0)

        visited[I][J] = 1
        
        for k in range(4):
            try:
                if I+dx[k]>=0 and J+dy[k]>=0:

                    if la[I+dx[k]][J+dy[k]] == 0 and visited[I+dx[k]][J+dy[k]] != 1:
                        Q.append((I+dx[k],J+dy[k]))

                    elif la[I+dx[k]][J+dy[k]] == 3:
                        return 1
            except:
                pass
    else:
        return 0


for tc in range(int(input())):
    n = int(input())
    la = [list(map(int, input())) for _ in range(n)]
    Q = []
    visited = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if la[i][j] == 2:
                I = i
                J = j
    
    Q.append((I,J))

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    print(f'#{tc+1}',maze())
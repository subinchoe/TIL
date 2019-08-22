# Queue

> 대부분 FIFO

- 파스칼의 삼각형 (어제 문제 리뷰)

```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    print("#{}".format(tc))
    for i in range(N):
        for j in range(i+1):
            if j == 0 or i == j:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
            print(arr[i][j], end=" ")
        print()
                
#    print("#{}".format(tc))
#    for i in range(N):
#        for j in range(i+1):
#            print(arr[i][j], end=" ")
#        print() 
```

- queue

```python
q = [0] * 10
front = -1
rear = -1

rear += 1
q[rear] = 1  # enqueue(1)

rear += 1
q[rear] = 2  # enqueue(2)

rear += 1
q[rear] = 3  # enqueue(3)

while (front != rear):  # q is not empty()
    front += 1
    print(q[front])
```

```python
# BFS 트리 문제 (반복구조의 DFS와 비슷함. stack에 넣느냐, queue에 넣느냐)
# 이 구조를 외워둘 것!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
q = [0] * 9 # 큐 생성
front = -1
rear = -1
rear += 1 # enq(1) 시작점 인큐
q[rear] = 1 # enq(1)
visited[1] = 1 # 시작점 방문 표시

while(front != rear): # 큐가 비어있지 않으면
    front += 1
    t = q[front] # 디큐
    # t에 인접이고 방문하지 않은 정점이면
    # 주어진 상황에 맞게 완성
    # t 주변의 모든 i에 대해
    if visited[i] == 0 and t에 i가 인접:
        ...# enq[i]
        visited[i] = visited[t] + 1
```

> DFS는 출발지가 한 곳으로 정해짐. 만약 여러 곳으로 정해진다면 각각 돌려야 함.
>
> BFS는 출발지가 여러 곳으로 정해짐 (최단 거리)

```python
# bfs 문제
def bfs(i, j, N):
    global maze
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    # 초기화
    q = []  # 큐 생성
    visited = [[0] * N for _ in range(N)]  # visited 생성
    q.append([i, j])  # 시작점 인큐
    visited[i][j] = 1  # 시작점 방문 표시
    # maze를 시작으로 하면? 벽의 1번과 시작의 1번이 구분이 안 간댕.
    # 탐색
    while(len(q) != 0):  # 큐가 비어있지 않으면 반복
        n = q.pop(0)  # 디큐
        i, j = n[0], n[1]
        if maze[i][j] == 3:  # visit()
            return visited[i][j] - 2  # 출발점과 도착점을 빼야 해서 - 2를 함
        # i, j에 인접하고 방문하지 않은 칸을 인큐
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni >= 0 and ni < N and nj >= 0 and nj < N:  # 미로를 벗어나지 않았고
                if maze[ni][nj] != '1' and visited[ni][nj] == 0:  # 벽이 아니고, 방문하지 않은 칸이면
                    q.append([ni, nj])  # 인큐
                    visited[ni][nj] = visited[i][j] + 1  # 방문 표시
    return 0
```

- 문제

```python
1. 1이 3개 연속된 경우는 몇 개?

주어진 리스트와 같은 길이의 used 리스트 생성
for i :0 -> N-3
    # arr[i]가 1이고 다른 연속 구간에 포함되지 않으면 1이 몇 개 연속인지 확인
    m = i # 연속된 1인지 확인하는 위치
    w = 0 # 연속된 1의 길이
    while(word[m]==1 and used[m]==0):
        used[m] = 1 # 연속된 1인지 확인된 구간 
        m += 1
        w += 1
    if w == K:
        cnt += 1
```


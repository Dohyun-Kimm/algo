# 15686 치킨거리
# 치킨거리 = 집과 가장 가까운 치킨집
# 도시의 치킨 거리 = sum(치킨거리)


#  0 - 빈칸 , 1 - 집, 2 - 치킨집
def dist(row1,col1,row2,col2):
    return abs(row1-row2) + abs(col1-col2)

N, M = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(5)]
# print(graph)
# 치킨 개수 M 
# 1 인 좌표 찾아서 각 점에서 bfs, dfs 둘중하나 하기. - bfs
# 2 를 발견한 시점에 1 좌표와 거리 구하기.
# 탈출 조건......
# 1. 이중 for 문 으로 모든 1인 좌표에서 시작하기
for i in range(N):

# 2. 1인 지점에서 bfs
# 3. 2를 발견하면 dist로 거리구하기.
# 4. 최소 치킨 거리를 구하고 도시 치킨 거리에 더하기
# 5. 출력


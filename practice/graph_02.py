'''
240406
너비 우선 탐색 순회

너비 우선 탐색으로 모든 노드를 순회하는 함수 solution()을 작성하세요.
시작 노드는 매개변수 start로 주어집니다.
graph는 (출발 노드, 도착 노드) 쌍들이 들어 있는 리스트입니다.
반환값은 그래프의 시작 노드부터 모든 노드를 너비 우선 탐색으로 진행한 순서대로 노드가 저장된 리스트입니다.

제약 조건
노드의 최대 개수는 100개입니다.
시작 노드부터 시작해서 모든 노드를 방문할 수 있는 경로가 항상 있습니다.
그래프의 노드는 숫자입니다.

입출력 예
graph                                                                               start   return
[(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (5, 8), (6, 9), (7, 9)]    1       [1, 2, 3, 4, 5, 6, 7, 8, 9]
[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)]                                            1       [1, 2, 3, 4, 5, 0]
'''
from collections import defaultdict, deque
def solution(graph, start) :
    nodes = defaultdict(list)

    for node in graph :
        nodes[node[0]].append(node[1])

    visited = defaultdict(bool)
    visited[start] = True
    queue = deque()
    queue.append(start)

    answer = [start]

    while queue :
        node = queue.popleft()

        route = nodes[node]

        for i in route :
            if not visited[i] :
                queue.append(i)
                visited[i] = True
                answer.append(i)

    return answer




graph, start = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)]    , 1
print(solution(graph, start))
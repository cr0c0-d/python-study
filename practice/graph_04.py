'''
240406
벨만-포드 알고리즘

벨만-포드 알고리즘을 구현한 solution() 함수를 구현하세요.
graph의 각 데이터는 리스트입니다.
첫 번째 데이터는 0번 노드 기준으로 연결된 노드 정보, 두 번째 데이터는 1번 노드 기준으로 연결된 노드 정보입니다.
노드 정보의 구성은 (노드, 가중치)와 같습니다.
source는 시작 노드입니다.
반환값은 최단 거리를 담은 distance 리스트와 최단 거리와 함께 관리할 직전 노드 predecessor를 리스트에 차례대로 담아서 [distance, predecessor] 형식으로 반환하면 됩니다.
predecessor에서 시작 노드는 None으로 표시합니다. 만약 음의 가중치 순회가 있다면 [-1]을 반환하세요.
음의 가중치 순회란 순환하면 할수록 가중치의 합이 적어지는 순회를 말합니다.

제약 조건
노드의 최대 개수는 100개입니다.
각 간선의 가중치는 -100 이상 100 이하입니다.

입출력 예
graph                                                                           source  return
[[(1, 4), (2, 3), (4, -6)], [(3, 5)], [(1, 2)], [(0, 7), (2, 4)], [(2, 2)]]     0       [[0, -2, -4, 3, -6], [None, 2, 4, 1, 0]]
[[(1, 5), (2, -1)], [(2, 2)], [(3, -2)], [(0, 2), (1, 6)]]                      0       [-1]
'''
def solution(graph, source) :
    n = len(graph)
    distance = [float("inf") for _ in range(n)]
    predecessor = [None for _ in range(n)]
    distance[source] = 0

    for i in range(n-1) :
        for mid in range(n) :
            for end, cost in graph[mid] :
                # 기록된 현재 노드의 최단거리 > (source부터 node까지의 거리 + node부터 연결된 각 노드까지의 거리)
                if distance[end] > distance[mid] + cost :
                    distance[end] = distance[mid] + cost    # 최단거리 갱신
                    predecessor[end] = mid  # 직전 노드 기록

    # 음의 순환이 있는지 확인하는 과정
    # 노드 개수-1만큼 반복한 이후에도 변화가 있으면 음의 순환이 있는 것
    for mid in range(n) :
        for end, cost in graph[mid] :
            if distance[end] > distance[mid] + cost :   # 음의 순환이 있음
                return [-1]
            
    return [distance, predecessor]


graph, source = [[(1, 5), (2, -1)], [(2, 2)], [(3, -2)], [(0, 2), (1, 6)]] , 0
print(solution(graph, source))
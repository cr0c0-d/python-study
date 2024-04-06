'''
240406
다익스트라 알고리즘

주어진 그래프와 시작 노드를 이용하여 다익스트라 알고리즘을 구현하는 solution() 함수를 작성하세요.
인수는 graph, start 총 2개 입니다.

graph는 딕셔너리로 주어지며 노드의 연결 정보와 가중치가 저장되어 있습니다.
예를 들어 {'A':{'B':2, 'C':5}}이면 A는 B, C에 각각 가중치 2, 5로 연결되어 있는 것입니다.

start는 문자열로 주어지며 출발 노드를 의미합니다.
반환값은 시작 노드부터, 각 노드까지 최소 비용과 최단 경로를 포함한 리스트입니다.

제약 조건
그래프의 노드 개수는 최대 10,000개입니다.
각 노드는 0 이상의 정수로 표현합니다.
모든 가중치는 0 이상의 정수이며 10,000을 넘지 않습니다.

입출력의 예
graph                                               start   return
{'A':{'B':9, 'C':3}, 'B':{'A':5}, 'C':{'B':1}}      'A'     [{'A':0, 'B':4, 'C':3}, {'A':['A'], 'B':['A', 'C', 'B'], 'C':['A', 'C']}]
{'A':{'B':1}, 'B':{'C':5}, 'C':{'D':1}, 'D':{}}     'A'     [{'A':0, 'B':1, 'C':6, 'D':7}, {'A':['A'], 'B':['A', 'B'], 'C':['A', 'B', 'C'], 'D':['A', 'B', 'C', 'D']}]
'''
# 우선순위 큐(heapq) 
import heapq

def solution(graph, start) :
    # start부터 각 노드까지의 최소 비용, 그 경로
    least_cost = {name : float("inf") for name in graph.keys()}     # 각 노드의 최소 비용을 기록할 딕셔너리 (최소 비용을 찾아야 하므로 값은 무한대로 초기화)
    
    least_cost[start] = 0
    path = { start : [start] }    # 최단 경로 저장하는 딕셔너리(시작 노드 기록)

    queue = []
    heapq.heappush(queue, [least_cost[start], start])   # 시작노드를 큐에 삽입
    

    while queue :
        cost, cur = heapq.heappop(queue)    # 우선순위 큐, 오름차순으로 우선순위 반환

        for node, next_cost in graph[cur].items() : # 연결된 노드들의 노드와 가중치
            if least_cost[node] > cost + next_cost :  # 기록된 최소비용보다 (현재 노드의 최소비용 + 해당 노드까지의 가중치)가 더 작으면
                least_cost[node] = cost + next_cost   # 최소비용 갱신
                path[node] = path[cur] + [node]  # 경로 기록 (현재 노드까지의 경로 + 해당 노드)
                heapq.heappush(queue, [least_cost[node], node]) # 우선순위 노드에 푸시

    answer = [least_cost, path]
    return answer




graph, start = {'A':{'B':9, 'C':3}, 'B':{'A':5}, 'C':{'B':1}}, 'A'
print(solution(graph, start))

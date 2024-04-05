'''
240405
깊이 우선 탐색 순회

깊이 우선 탐색으로 모든 그래프의 노드를 순회하는 함수 solution()을 작성하세요.
시작 노드는 start로 주어집니다. graph는 [출발 노드, 도착 노드] 쌍들이 들어 있는 리스트입니다.
반환값은 그래프의 시작 노드부터 모든 노드를 깊이 우선 탐색으로 진행한 순서대로 노드가 저장된 리스트입니다.

제약 조건
노드의 최대 개수는 100개를 넘지 않습니다.
시작 노드부터 시작해서 모든 노드를 방문할 수 있는 경로가 항상 있습니다.
그래프의 노드는 문자열입니다.

입출력 예
graph                                                                       start   return
[['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E']]                            'A'     ['A', 'B', 'C', 'D', 'E']
[['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['E', 'F']]    'A'     ['A', 'B', 'D', 'E', 'F', 'C']
'''
def solution(graph, start) :
    graph_dict = { }
    for node in graph :
        graph_dict.setdefault(node[0], []).append(node[1])

    stack = [start]
    visited = {name : False for name in graph_dict.keys()}
    answer = []
    while stack :
        cur = stack.pop()
        if visited[cur] :
            continue
        answer.append(cur)
        visited[cur] = True

        for i in sorted(graph_dict[cur], reverse=True) :
            stack.append(i)

    return answer




graph, start = [['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['E', 'F']], 'A'
print(solution(graph, start))
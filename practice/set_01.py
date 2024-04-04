'''
240404 집합

간단한 유니온-파인드 알고리즘 구현하기
권장 시간 복잡도 O(N)

상호배타적 집합을 표현하고 관리하는 데 다음 두 연산이 필요합니다.
union(x, y) : x와 y가 속한 두 집합을 합칩니다.
find(x) : x가 속한 집합의 대표 원소를 찾습니다.

operations라는 배열은 수행할 연산을 의미합니다.
연산 종류는 2개 입니다.
['u', 1, 2]는 노드 1과 노드 2에 대해 union 연산 수행
['f', 3] 노드 3의 루트 노드 찾기, find 연산 수행

초기의 노드는 부모 노드를 자신의 값으로 설정했다고 가정하며,
여기서는 각 집합의 루트 노드를 기준으로 루트 노드가 작은 노드를 더 큰 노드의 자식으로 연결하는 방법을 사용합니다.
operations에 있는 연산을 모두 수행한 후 집합의 개수를 반환하는 solution() 함수를 구현해주세요.

제약 조건
0 <= k <= 1,000 : 노드의 개수
1 <= len(operations) <= 100,000
operations[i][0]은 문자열 'u' 또는 'f' 중 하나
'u'는 union 연산, union 연산 뒤로는 두 개의 정수 x, y가 나옴
'f'는 find 연산, find 연산 뒤로는 하나의 정수 x가 나옴
x와 y는 0 이상 k-1 이하의 정수
연산은 항상 유효함
- 즉, union, find 연산의 인수는 상호배타적 집합 내에 있는 노드 번호

입출력 예
k   operations                              result
3   [['u', 0, 1], ['u', 1, 2], ['f', 2]]    1
4   [['u', 0, 1], ['u', 2, 3], ['f', 0]]    2
'''
def solution(k, operations) :
    node = list(range(k))
    n = k # 집합의 개수, 초기에는 k개

    for op in operations :
        if op[0] == 'u' :
            union(op[1], op[2], node)
        elif op[0] == 'f' :
            find(op[1], node)

    n = len(set(find(i, node) for i in node))
    return n

def find(x, node) :
    nx = node[x]
    if nx != x :
        return find(nx, node)
    else :
        return x


def union(x, y, node) :
    root1 = find(x, node)
    root2 = find(y, node)
    node[root1] = root2


k, operations = 4, [['u', 0, 1], ['u', 2, 3], ['f', 0]]
print(solution(k, operations))

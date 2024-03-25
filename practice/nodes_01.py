'''
트리 순회

이진 트리를 표현한 리스트 nodes를 인자로 받습니다.
해당 이전 트리에 대하여 전위 순회, 중위 순회, 후위 순회 결과를 반환하는 solution() 함수를 구현하세요.

제약 조건
입력 노드값의 개수는 1개 이상 1,000개 이하이다.
노드값은 정수형이며, 중복되지 않는다.

입출력의 예
nodes                   return
[1, 2, 3, 4, 5, 6, 7]   ["1 2 4 5 3 6 7', "4 2 5 1 6 3 7", "4 5 2 6 7 3 1"]
'''

def solution(nodes) :
    answer = [ ]
    answer.append(preorder(nodes, 0)[1:])
    answer.append(inorder(nodes, 0)[1:])
    answer.append(postorder(nodes, 0)[1:])
    return answer


def preorder(nodes, index) :
    if index < len(nodes) :
        return " " + str(nodes[index]) + preorder(nodes, index * 2 + 1) + preorder(nodes, index * 2 + 2)
    else :
        return ""


def inorder(nodes, index) :
    if index < len(nodes) :
        return inorder(nodes, index * 2 + 1) + " " + str(nodes[index]) + inorder(nodes, index * 2 + 2)
    else :
        return ""


def postorder(nodes, index) :
    if index < len(nodes) :
        return postorder(nodes, index * 2 + 1) + postorder(nodes, index * 2 + 2) + " " + str(nodes[index])
    else :
        return ""




nodes = [1, 2, 3, 4, 5, 6, 7]
print(solution(nodes))

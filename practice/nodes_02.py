'''
240326
이진 탐색 트리 구현

첫 번째 인수 lst를 이용하여 이진 탐색 트리를 생성하고,
두 번째 인수 search_lst에 있는 각 노드를 이진 탐색 트리에서 찾을 수 있는지 확인하여
True 혹은 False를 담은 리스트 result를 반환하는 함수  solution()을 작성하세요.

제약 조건
lst의 노드는 정수로 이루어져 있으며 1,000,000개를 초과하지 않습니다.
이진 탐색 트리의 삽입과 탐색 기능을 구현해야 합니다.
search_lst의 길이는 10 이하입니다.

입출력의 예
lst                         search_lst          answer
[5, 3, 8, 4, 2, 1, 7, 10]   [1, 2, 5, 6]        [True, True, True, False]
[1, 3, 5, 7, 9]             [2, 4, 6, 8, 10]    [False, False, False, False, False]
'''
def solution(lst, search_lst) :
    result = [ ]
    bst = BST()
    for i in lst :
        bst.insert(i)

    for i in search_lst :
        if bst.search(i) :
            result.append(True)
        else :
            result.append(False)

    return result

class Node :
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BST :
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root :
            self.root = Node(key)
        else :
            curr = self.root
            while True :
                if key < curr.val :
                    if curr.left :
                        curr = curr.left
                    else :
                        curr.left = Node(key)
                        break

                else :

                    if curr.right :
                        curr = curr.right

                    else :
                        curr.right = Node(key)
                        break

    def search(self, key):
        curr = self.root
        while curr and curr.val != key :
            if key < curr.val :
                curr = curr.left
            else :
                curr = curr.right

        return curr


lst, search_lst = [1, 3, 5, 7, 9], [2, 4, 6, 8, 10]
print(solution(lst, search_lst))

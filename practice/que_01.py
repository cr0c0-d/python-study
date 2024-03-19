'''
N명의 사람이 원 형태로 서 있습니다.
각 사람은 1부터 N까지 번호표를 갖고 있습니다.
그리고 임의의 숫자 K가 주어졌을 때 다음과 같이 사람을 없앱니다.

- 1번 번호표를 가진 사람을 기준으로 K번째 사람을 없앱니다.
- 없앤사람 다음 사람을 기준으로 하고 다시 K번째 사람을 없앱니다.

N과 K가 주어질 때 마지막에 살아있는 사람의 번호를 반환하는 solution() 함수를 구현하세요.

제약조건
- N과 K는 1이상 1000이하의 자연수입니다.

입출력 예
N	K	return
5	2	3
'''
from collections import deque

#원형 큐로 풀어보기
def solution(N, K) :

    arr = deque(i+1 for i in range(N))

    while len(arr) != 1 :
        arr.rotate(-K+1)
        arr.popleft()

    return arr.pop()

# 선형 큐로 풀어보기
def solution2(N, K) :
    queue = deque(i+1 for i in range(N))

    while len(queue) != 1 :
        for _ in range(K-1) :
            queue.append(queue.popleft())
        queue.popleft()

    return queue.pop()



N = 5
K = 2
print(solution(N, K))
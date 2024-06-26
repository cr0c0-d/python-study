'''
정수 배열을 하나 받습니다.
배열의 중복값을 제거하고 배열 데이터를 내림차순으로 정렬해서 반환하는 solution()함수를 구현하세요

제약조건
배열 길이는 2 이상 1,000 이하입니다.
각 배열의 데이터 값은 -100,000 이상 100,000 이하입니다.

입출력 예
[4, 2, 2, 1, 3, 4]      [4, 3, 2, 1]
[2, 1, 1, 3, 2, 5, 4]   [5, 4, 3, 2, 1]
'''

def solution(arr) :
    arr2 = list(set(arr))   # set() : 집합을 생성하는 내장함수. 집합은 중복값을 허용하지 않으므로 중복값 제거함
    arr2.sort(reverse=True)
    return arr2

arr1 = [4, 2, 2, 1, 3, 4]
result = solution(arr1)
print(result)

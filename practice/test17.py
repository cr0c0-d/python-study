'''
정수 배열 numbers가 주어집니다.
numbers에서 서로 다른 인덱스에 있는 2개의 수를 뽑아 더해 만들 수 있는 모든 수를 배열에 오름차순으로 담아 반환하는 solution() 함수를 완성하세요.

제약 조건
numbers의 길이는 2 이상 100 이하입니다.
numbers의 모든 수는 0 이상 100 이하입니다.

입출력의 예
numbers             result
[2, 1, 3, 4, 1]     [2, 3, 4, 5, 6, 7]
[5, 0, 2, 7]        [2, 5, 7, 9, 12]
'''

def solution(arr) :
    n = len(arr)
    result = []

    for i in range(n) :
        for j in range(n) :
            if(i != j) :
                result.append(arr[i] + arr[j])

    result = list(set(result))
    result.sort()

    return result

'''
첫 파이썬 치고 나름 잘했는데 이러면 됨ㅠㅠ

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))
'''
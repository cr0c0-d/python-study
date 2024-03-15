'''
정수 배열을 정렬해서 반환하는 solution() 함수를 완성하세요

제약조건
* 정수 배열의 길이는 2 이상 10^5 이하입니다.
* 정수 배열의 각 데이터 값은 -100,000 이상 100,000 이하입니다.

입출력 예
입력                  출력
[1, -5, 2, 4, 3]        [-5, 1, 2, 4, 3]
[2, 1, 1, 3, 2, 5, 4]   [1, 1, 2, 2, 3, 4, 5]
[6, 1, 7]               [1, 6, 7]
'''
import time

def solution(arr) :
    if len(arr) < 2 :
        return
    else :
        arr.sort()
        return arr

def solution2(arr) :
    length = len(arr)
    for i in range(length) :
        for j in range(length - i - 1) :
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

def measure_time(func, arr) : # 시간을 측정하고 뒤집힌 배열 반환
    start_time = time.time()
    result = func(arr)
    end_time = time.time()
    return end_time - start_time, result



arr1 = [1, -5, 2, 4, 3]

s1_time, s1_result = measure_time(solution, arr1)
print('첫 번째 코드 실행 시간 : ', format(s1_time, ".10f"))

s2_time, s2_result = measure_time(solution2, arr1)
print('두 번째 코드 실행 시간 : ', format(s2_time, ".10f"))

print('두 코드의 결과가 동일한지 확인 : ',s1_result == s2_result)


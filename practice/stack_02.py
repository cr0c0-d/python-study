'''
240318
10진수를 2진수로 변환하기

10진수를 입력받아 2진수로 변환해 반환하는 solution() 함수를 구현하세요.

입출력 예
decimal     return
10          1010
27          11011
12345       11000000111001
'''

def solution(decimal) :
    arr = []
    answer = ""

    while decimal > 0 :
        arr.append(decimal % 2)
        decimal //= 2

    # arr.reverse()
    # for num in arr :
    #     answer += str(num)
    
    answer = ''.join([str(n) for n in arr])     # 문자열 합칠땐 join()이 효율적!      연결자.join(반복자)
    
    # 이렇게 하면 더 간결
    # while arr :
    #     answer += arr.pop()

    return answer

decimal = 12345
print(solution(decimal))
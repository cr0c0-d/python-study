'''
240318
괄호 짝 맞추기

소괄호는 짝을 맞춘 열린 괄호 '('와 닫힌 괄호 ')'로 구성합니다.
문제에서는 열린 괄호나 닫힌 괄호가 마구 뒤섞인 문자열을 줍니다.
이 때 소괄호가 정상으로 열고 닫혔는지 판별하는 solution()함수를 구현하세요.
만약 소괄호가 정상적으로 열고 닫혔다면 True를, 그렇지 않다면 False를 반환하세요.

제약조건
열린 괄호는 자신과 가장 가까운 닫힌 괄호를 만나면 상쇄됩니다.
상쇄 조건은 열린 괄호가 먼저 와야 하고, 열린 괄호와 닫힌 괄호 사이에 아무것도 없어야 합니다.
더 상쇄할 괄호가 없을 때까지 상쇄를 반복합니다.

입출력 예
s           return
(())()      True
((())()     False
'''

def solution(str) :
    answer = []

    for c in str :
        if c == '(' :
            answer.append(c)
        else :
            if len(answer) == 0 :   # if answer : return False else: answer.pop()  => 이렇게 해도 됨
                return False
            else:
                answer.pop()

    if len(answer) != 0 : # if answer : return True else: return False  => 이렇게 해도 됨
        return False
    else :
        return True


str = ")()()"
print(solution(str))





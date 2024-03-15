# 함수

# 함수 정의
def addNum(num1, num2) :
    result = num1 + num2
    return result

# 함수 호출
ret = addNum(5, 10)
print(ret)

# 람다식
# 함수를 간단하게 표현하는 방법
# 익명함수 생성 => 코드에서 딱 한 번 실행할 목적 or 다른 함수의 인수

# 람다식 정의
# 변수에 할당하기
addNum2 = lambda x, y : x + y
print(addNum2(5, 4))    # 9

# 인수로 람다식 넘기기
num = [1, 2, 3, 4, 5]
squares = list(map(lambda x : x ** 2, num)) # 람다식 넘기기
print(squares)  # [1, 4, 9, 16, 25]

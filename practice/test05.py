# 논리연산자
a = 10
b = 11
c = 12
d = 10

print('not(a < 10)의 결과는 : ', not(a < 10))
print('(a < b) and (a > c)의 결과는 : ', (a < b) and (a > c))
print('(a >= c) or (a == d)의 결과는 : ', (a >= c) or (a == d))

"""
not : 반대 -> java의 !
and : 그리고 -> java의 &&
or : 또는 -> java의 ||
"""


money = int(input('돈을 넣어주세요.'))
count = int(input('몇 장 드릴까요?'))
ticket = 12000

money -= (ticket * count)
change = '거스름돈 : ' + str(money)

result = money < 0 and '잔액이 부족합니다. 금액을 투입해주세요. ' or change
print(result)

"""
삼항연산자

(조건) and (결과1) or (결과2)
java => (조건) ? (결과1) : (결과2)
"""
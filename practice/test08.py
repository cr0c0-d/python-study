#packing 연산
# 변수명 앞에 * 연산자 붙이면 복수의 값 할당

v1, *v2 = 1, 2, 3, 4, 5
print(v1)
print(v2)


print("***********")


*v1, v2 = 1, 2, 3, 4, 5
print(v1)
print(v2)


print("***********")


*v1, v2, v3 = 1, 2, 3, 4, 5
print(v1)
print(v2)
print(v3)


print("***********")


v1, *v2, v3 = 1, 2, 3, 4, 5
print(v1)
print(v2)
print(v3)

# *v1, *v2, v3 = 1, 2, 3, 4, 5      => 에러! * 연산자는 복수 사용 불가

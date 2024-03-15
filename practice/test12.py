# 튜플
# 이뮤터블 객체
# 리스트에 모든 기능이 있는데 왜 쓸까?
# => 값이 변경되지 않아야하는 데이터에 사용하여 실수 방지

# 튜플 초기화
my_tuple = (1, 2, 3)

# 인덱싱
print(my_tuple[0])  # 1
print(my_tuple[1])  # 2
print(my_tuple[2])  # 3

# 슬라이싱
print(my_tuple[1:])     # (2, 3)
print(my_tuple[:2])     # (1, 2)
print(my_tuple[1:2])    # (2,)

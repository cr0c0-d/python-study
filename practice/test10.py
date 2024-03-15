# 리스트

# 리스트 선언
my_list = [1, 2, 3, 4, 5]
my_list2 = [1, 3, 5] + [7, 9]
my_list3 = list(my_list)

print(my_list)  # [1, 2, 3, 4, 5]
print(my_list2) # [1, 3, 5, 7, 9]
print(my_list3) # [1, 2, 3, 4, 5]


# 리스트 인덱싱

my_list4 = [1, 2, 4]

# 값 추가
my_list4.append(6)
print(my_list4)     # [1, 2, 4, 6]

# 인덱싱으로 값 삭제
del my_list4[2]
print(my_list4) # [1, 2, 6]


# 리스트 슬라이싱
# listName[a:b]     a 이상, b 미만

my_list = [1, 2, 3, 4, 5]

print(my_list[0:2])     # [1, 2]
print(my_list[1:])      # [2, 3, 4, 5]
print(my_list[3:4])     # [4]
print(my_list[-4:-2])   # [2, 3]

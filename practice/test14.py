# 길이가 6인 정수형 배열 선언하기
arr = [0, 0, 0, 0, 0, 0]
arr = [0] * 6

arr = list(range(6))    # [0, 1, 2, 3, 4, 5]

arr = [0 for _ in range(6)]  # [0, 0, 0, 0, 0, 0]

# 2차원 배열 선언
arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

# arr[2][3]에 저장된 값 출력
print(arr[2][3])    # 12

# arr[2][3]에 저장된 값을 15로 변경
arr[2][3] = 15

#변경된 값 출력
print(arr[2][3])    # 15

# 리스트 컴프리헨션 선언
arr = [[i] * 4 for i in range(3)]   # [[0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 2, 2]]


# 리스트 기법
my_list = [1, 2, 3]

# 데이터 삽입

# append() : 배열의 맨 끝에 데이터 추가
my_list.append(4)   # [1, 2, 3, 4]

# + 연산자로 데이터 추가
my_list = my_list + [5, 6]  # [1, 2, 3, 4, 5, 6]

# insert() : 특정 위치에 데이터 삽입
my_list.insert(2, 100)   # [1, 2, 100, 3, 4, 5, 6]


# 데이터 삭제

# pop() : 인덱스를 받아 삭제하고 값 반환
popped_element = my_list.pop(2) # 100
print(my_list)  # [1, 2, 3, 4, 5, 6]

# remove() : 인수로 받은 값이 처음 등장하는 위치의 값 삭제 (인수로 인덱스 받는거 xx 값 받는거 oo)
my_list.append(2)   # [1, 2, 3, 4, 5, 6, 2]     =>  2가 중복임
my_list.remove(2)   # [1, 3, 4, 5, 6, 2]    => 가장 앞의 2를 삭제함

# 리스트 컴프리헨션
# 기존 리스트를 이용해 새 리스트를 생성

# 리스트에 제곱 연산 적용 예
squares = [num ** 2 for num in my_list] # [1, 9, 16, 25, 36, 4]
## 기존 my_list는 그대로임! 새로운 리스트를 생성한 것


# 이외 메서드
# len() : 리스트 길이(데이터 개수)
print(len(my_list))     # 6

# index() : 특정 데이터가 처음 등장한 인덱스 반환
print(my_list.index(5))     # 3

# sort() : 정렬
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)

# count() : 특정 값의 개수
# 딕셔너리
# 키 key , 값 value   해시테이블
# 뮤터블 객체

# 딕셔너리 초기화
my_dict = { }

# 딕셔너리 값 삽입
my_dict["apple"] = 1
my_dict["banana"] = 2
my_dict["orange"] = 3

print(my_dict)      # {'apple': 1, 'banana': 2, 'orange': 3}


# 딕셔너리 검색
key = "apple"
if key in my_dict :
    value = my_dict[key]
    print(f"{key} : {value}") # apple : 1
else:
    print(f"{key}는 딕셔너리에 존재하지 않습니다.")

# 딕셔너리 수정
my_dict["banana"] = 4
print(my_dict)  # {'apple': 1, 'banana': 4, 'orange': 3}

# 딕셔너리 삭제
del my_dict["orange"]
print(my_dict)  # {'apple': 1, 'banana': 4}

# 없는 키로 삭제하려는 경우 예외 발생! 예외처리 필요

my_dict = {'apple': 1, 'banana': 2, 'cherry': 3}

key = "kiwi" # my_dict에 없는 키

if key in my_dict:
    print(f"값 : {my_dict[key]}")
else:
    print(f"'{key}' 키가 딕셔너리에 없습니다.")



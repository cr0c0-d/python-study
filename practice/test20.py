'''
240406
defaultdict 클래스

키가 없을 때 기본값을 defaultdict 형태로 지정
defaultdict(list) ---> 기본값 []로 초기화
'''
from collections import defaultdict

# defaultdict를 생성하고 초깃값으로 str('') 지정
my_dict_str = defaultdict(str)

# defaultdict를 생성하고 초깃값으로 list([]) 지정
my_dict_list = defaultdict(list)

# 각 defaultdict에서 키에 접근하여 값 확인
print(my_dict_str['key'])   # 출력 : ''
print(my_dict_list['key'])  # 출력 : []

# 값 추가 및 조작 수행
my_dict_str['key'] += 'Hello'
my_dict_list['key'].append(1)

# 각 defaultdict에서 키에 접근하여 값 확인
print(my_dict_str['key'])   # 출력 : 'Hello'
print(my_dict_list['key'])  # 출력 : [1]


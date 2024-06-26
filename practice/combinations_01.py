from itertools import combinations

# Combinations : 모든 가능한 조합을 생성
arr = ['A', 'B', 'C']
comb = combinations(arr, 2)

for i in comb :
    print(i)

# ('A', 'B')
# ('A', 'C')
# ('B', 'C')

print("#####################")

# 순서가 다르면 다른 조합으로 간주함

arr = ['A', 'B', 'C', 'A']
comb = combinations(arr, 2)

for i in comb :
    print(i)

# ('A', 'B')
# ('A', 'C')
# ('A', 'A')
# ('B', 'C')
# ('B', 'A')
# ('C', 'A')

print("#####################")

# 문자열도 가능함
# 튜플, 셋, 딕셔너리의 키로도 사용가능(iterable한 객체)

str = "ABC"
comb = combinations(str, 2)

for i in comb :
    print(i)


print("#####################")

from itertools import permutations
# 순열(permutations)와는 다르다.
# ['A', 'B', 'C'] 에서의 결과 차이

arr = ['A', 'B', 'C']
perm = permutations(arr, 2)
for i in perm :
    print(i)
# ('A', 'B')
# ('A', 'C')
# ('B', 'A')
# ('B', 'C')
# ('C', 'A')
# ('C', 'B')
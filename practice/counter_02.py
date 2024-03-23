from collections import Counter

# Counter 객체의 메서드

print("#### 1. elements() ####")

# 1. elements()
# Counter 객체 내의 요소를 반복 가능한 형태로 반환
# 각 요소는 등장 횟수만큼 반복
# 반환 순서는 임의
c = Counter('abcdeabcdabcaba')
print(list(c.elements()))   # ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'd', 'd', 'e']


print("#### 2. most_common([n]) ####")

# 2. most_common([n])
# 가장 흔히 등장하는 요소를 등장 횟수와 함께 반환
# n을 지정하면, 상위 n개의 가장 흔한 요소를 반환
c = Counter('abcdeabcdabcaba')
print(c.most_common())  # [('a', 5), ('b', 4), ('c', 3), ('d', 2), ('e', 1)]
print(c.most_common(3)) # [('a', 5), ('b', 4), ('c', 3)]


print("#### 3. subtract([iterable or mapping]) ####")

# 3. subtract([iterable-or-mapping])
# 다른 Counter 객체나 반복가능한 객체의 요소를 현재 Counter 객체에서 뺀다
c = Counter('abcdeabcdabcaba')
d = Counter('abcaba')

print(f"c : {c} / d : {d}") # c : Counter({'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1}) / d : Counter({'a': 3, 'b': 2, 'c': 1})

c.subtract(d)
print(c)    # Counter({'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 1})


print("#### 4. update([iterable-or-mapping]) ####")

# 4. update([iterable-or-mapping])
# Counter 객체에 다른 Counter 객체나 반복가능한 객체의 요소를 추가한다
c = Counter('abcde')
c.update('abc')
print(c)    # Counter({'a': 2, 'b': 2, 'c': 2, 'd': 1, 'e': 1})



print("#### 5. +, -, &, | ####")

# 5. +, -, &, |
# Counter 객체들 간의 연산
# + : 두 Counter 객체의 요소들의 등장 횟수를 합한다.
# - : A Counter 객체에서 B Counter 객체의 요소들의 등장 횟수를 빼고, 결과가 음수가 아닌 요소만 남긴다.
# & : 두 Counter 객체의 교집합(각 요소의 최소 등장 횟수)을 반환한다.
# | : 두 Counter 객체의 합집합(각 요소의 최대 등장 횟수)을 반환한다.
c = Counter('abcdeabcdabcaba')
d = Counter('abcaba')

print(f"c : {c} / d : {d}") # c : Counter({'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1}) / d : Counter({'a': 3, 'b': 2, 'c': 1})

print(c + d)  # Counter({'a': 8, 'b': 6, 'c': 4, 'd': 2, 'e': 1})
print(c - d)  # Counter({'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 1})
print(c & d)  # Counter({'a': 3, 'b': 2, 'c': 1})
print(c | d)  # Counter({'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1})
from collections import Counter

# Counter
# 객체의 수를 세어서 딕셔너리로 반환함
# 요소가 key, 등장 횟수가 value
arr = ['A', 'B', 'C', 'A', 'B', 'A']
print(Counter(arr))
# Counter({'A': 3, 'B': 2, 'C': 1})

str = "ABCDABCAB"
print(Counter(str))
# Counter({'A': 3, 'B': 3, 'C': 2, 'D': 1})

# iterable한 객체에 대해 모두 사용 가능
# 단, set의 경우 중복이 허용되지 않으므로 무의미 (모든 value가 1)
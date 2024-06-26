# 출력용 서식
# format(정수 혹은 실수, '전체자릿수.소수점자릿수<서식기호>')

print(format(123.456789, '10.3f'))  # f는 float, 전체 10자리, 소수점 3자리
print(format(123, '10d')) # d는 정수, 전체 10자리
print(format(123.4567, '.1E'))

# %format
# print('메시지 %서식기호' %(서식기호 매핑자료))
print('서식에 의한 자료 출력 %s %d %f' %('문자열', 10, 1.234))
print('나는 키가 %fcm이고, 에너지는 %d%%이다.' %(165, 100))

# {}.format()
# {매핑순서}.format()
print('이름 : {0}, 가격 : {1}'.format('마우스', 5000))
print('이름 : {}, 가격 : {}'.format('마우스', 5000))   # 서식과 대응자료의 수가 일치하면 인덱스는 생략 가능
print('이름 : {1}, 가격 : {0}'.format(5000, '마우스')) # 순서가 일치하지 않으면 인덱스 넣기
print('가격 : {0:,}'.format(50000000))    # 3자리마다 , 찍기

# f-String
# f {변수명 혹은 데이터}
name = '악어'
age = 30
print(f"안녕하세요, 저는 {name}이고 {age}살입니다")
print(f"{1+2+3} ::: {sum([1, 2])}")

# Raw String
print('aa\tbb')     # 원래 \t는 탭 문자로 취급되지만
print(r'aa\tbb')    # 문자열 앞에 r을 붙이면 Raw String으로 출력

print('c:\aa\abc.txt')  # \a때문에 제대로 출력되지 않지만
print(r'c:\aa\abc.txt') # r을 붙이면 해결 (경로 지정에 필수)

# 행 연결하기
# 코드 끝에 \를 붙이면 다음 행에 이어 쓸 수 있다
total = 2 + \
    3 * 4
print(total)

# 단 리스트는 \ 없이도 다음 행에 이어 쓸 수 있다
arr = ['a', 'b'
       , 'c']
print(arr)
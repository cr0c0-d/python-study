CHO_SUNG = ["ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]
JUNG_SUNG = ["ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅗ", "ㅘ", "ㅙ", "ㅚ", "ㅛ", "ㅜ", "ㅝ", "ㅞ", "ㅟ", "ㅠ", "ㅡ", "ㅢ", "ㅣ"]
JONG_SUNG = ["", "ㄱ", "ㄲ", "ㄳ", "ㄴ", "ㄵ", "ㄶ", "ㄷ", "ㄹ", "ㄺ", "ㄻ", "ㄼ", "ㄽ", "ㄾ", "ㄿ", "ㅀ", "ㅁ", "ㅂ", "ㅄ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]

# 한글 음절을 만드는 함수
def create_korean_char(chosung, jungsung, jongsung=""):
    chosung_index = CHO_SUNG.index(chosung)
    jungsung_index = JUNG_SUNG.index(jungsung)
    jongsung_index = JONG_SUNG.index(jongsung)

    # 한글 음절 코드 계산
    korean_char_code = 0xAC00 + ((chosung_index * 21) + jungsung_index) * 28 + jongsung_index
    return chr(korean_char_code)

# 한글 자모 합치기 함수
def combine_hangul(jamos):
    result = ""
    i = 0
    while i < len(jamos):
        chosung = jamos[i]
        i += 1
        if i < len(jamos):
            jungsung = jamos[i]

            i += 1
            jongsung = ''
            # 종성인지 다음 글자 초성인지 확인
            if i < len(jamos) :
                jongsung = jamos[i]
                i += 1
                if i < len(jamos) :
                    next_chr = jamos[i]

                    if ord("ㄱ") > ord(next_chr) or ord(next_chr) > ord("ㅎ") :  # 자음 범위가 아님 (jongsung은 다음 글자 초성)
                        jongsung = ""
                        i -= 1

            # 한글 문자로 합치기
            result += create_korean_char(chosung, jungsung, jongsung)
        else:
            break  # 중성이 없는 경우

    return result

# 예제 사용
print(combine_hangul("ㄱㅣㅁㅎㅕㅇㄹㅐㅂㅏㅂㅜ"))

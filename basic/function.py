# 함수 만들기
def english():
    print("영어과 입니다.")

english()

# 인자 전달
def math(a, b, eng):
    print("수학과 입니다.")
    print("%d + %d = %d" % (a, b, a + b))
    eng()

# 함수의 인자로 함수 전달
math(a=3, b=4, eng=english)

# return
def whois():
    name = "chaegeon"
    return name

namee = whois()
print(namee)
sentence = '나는 박진수 입니다'
print(sentence)

sentence2 = "파이썬을 배우고 있습니다."
print(sentence2)

sentence3= """          
나는 박진수 입니다,     띄어쓰기도 가능하다
파이썬을 배우고 있습니다.
"""
#""" """을 사용하면 4줄이 찍힌다.
print(sentence3)

sentence4 ="""알리바바에서 공부중입니다."""
print(sentence4)

print("a" + "b")
print("a","b")      # ,로 표현하면 띄어쓰기가 표현되어 출력 된다.

# 방법 1
print("나는 %d살 입니다." %20)        #%d 정수
print("나는 %s을 좋아해요." %"파이썬") #%s 문자열
print("APPLE 은 %c로 시작해요" % "A") #%c 문자 

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")

# %s 로만 적으면 
print("나는 %s살 입니다." %20)
print("나는 %s 색과 %s색을 좋아해요." %("파란", "빨간")) 
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")

#방법 2

print("나는 {}살 입니다.".format(20))
print("나는 {} 색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0} 색과 {1}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1} 색과 {0}색을 좋아해요.".format("파란", "빨간"))

#방법 3
print("나는 {age} 살이며, {color}색을 좋아해요.".format(age =20, color="빨간"))
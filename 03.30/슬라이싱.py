jumin = "991116-1234567"
#슬라이싱은 여기서 필요한 정보만 가져오는 것이다

print("성별 :" + jumin[7])
#[]안에 숫자는 01234567 순서로 카운팅해서 성별이 1이므로 7번째 자리 여서 7로함
print("연 : " + jumin[0:2]) #0~2직전까지 

print("월 : "+ jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 :" + jumin[0:6])
print("생년월일 :" + jumin[:6])

print("뒤 7자리" +jumin[7:14])
print("뒤 7자리" +jumin[:14])
print("뒤 7자리 (뒤에부터)" + jumin[-7:])
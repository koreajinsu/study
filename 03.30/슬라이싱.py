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

jumin = "991116-1196629"
#슬라이싱은 여기서 필요한 정보만 가져오는 것이다.

print("성별 :" + jumin[7])
# []안에 숫자는 0123245678 순서로 카운팅해서 성별이 1이므로 7번쨰 자리 여서 7로함
print("연 : " + jumin)


'''
산술 연산자: 산술 연산자는 기본적인 수학적 연산을 수행합니다.

+ : 덧셈
- : 뺄셈
* : 곱셈
/ : 나눗셈
% : 나머지 (모듈로 연산)


할당 연산자: 변수에 값을 할당하는 데 사용됩니다.
= : 할당


증가/감소 연산자: 변수 값을 증가시키거나 감소시킵니다.

++ : 증가 연산자
-- : 감소 연산자


비트 연산자: 비트 단위 연산을 수행합니다.
& : 비트 AND
| : 비트 OR
^ : 비트 XOR
~ : 비트 NOT
<< : 비트를 왼쪽으로 이동
>> : 비트를 오른쪽으로 이동


논리 연산자: 논리 연산을 수행합니다.
&& : 논리 AND
|| : 논리 OR
! : 논리 NOT


관계 연산자: 비교 연산을 수행하여 결과를 논리 값으로 반환합니다.
== : 같음
!= : 다름
> : 크다
< : 작다
>= : 크거나 같다
<= : 작거나 같다


조건부 연산자: 조건에 따라 값을 반환합니다.
? : : 삼항 조건 연산자
'''

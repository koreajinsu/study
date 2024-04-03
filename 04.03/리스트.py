#  리스트[]

# 지하철 칸 별로 10명, 30명
# subway =10
# sunway =20
# subway =30

#위에 내용과 동일 하다. 리스트 방법임
subway =[10,20,30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)
#조세호씨가 몇 번째 칸에 타고 있는가?
#왼쪽 부터 0,1,2~ 이렇게 이어진다.
print(subway.index("조세호"))


# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)

#정형돈을 유재석 / 조세호 사이에 태워본다.
subway.insert(1, "정형돈")
print(subway)

# # 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())  #총 3명을 꺼냈다.
# print(subway)

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
# 같은 이름의 사람이 몇 명 있는지 확인하기
subway.append("유재석") # 맨뒤에 유재석 추가
print(subway) #출력
print(subway.count("유재석")) #유재석이 몇 번 있는지 확인

print("\n")
# 정렬도 가능하다.
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

print("\n")
# 순서 뒤집기도 가능
num_list.reverse()
print(num_list)

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")

# 모두 지우기
num_list.clear()
print(num_list)

print("\n")
# 다양한 자료형 함께 사용 가능하다.
num_list = [5,2,4,3,1]
mix_list = ["조세호", 20, True]
print(mix_list)


print("\n")
#리스트 확장
num_list.extend(mix_list)
print(num_list)

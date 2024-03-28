#140 이상만 놀이기구를 탈 수있다.
#변수 먼저 만든다. TALL

#입력 함수로 키 입력을 만든다. INPUT                x
#키가 140 이상 또는 이하인지 구분해야된다. IF문      x
#키가 140이상이면 놀이기구 탈 수 있다.              x
#키가 140이하면 놀이기구 탈 수 없다.                x

tall = 0
tall = input('키를 입력해주세요. ')
tall = int(tall)
print(tall)

if( tall >= 140 ):
    print('놀이기구 입장 가능.')
    print('!!!!.')
else:
    print('놀이기구 못 탐.')




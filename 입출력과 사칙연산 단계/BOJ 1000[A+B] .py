a, b = [int(x) for x in input().split()]
print(a+b)

#          []: 리스트화함
#          이유_리스트화하지 않으면 입력된 숫자값이 문자로 취급 받기 때문.
#               cf. 111 + 222 -> 111222
#          입력된 값(input())을 구분하고(.split()) x에 입력하여 정수화한다.(int(x))
#          좀더 자세히 설명하면

a, b = [int(x) for x in input().split()]

#                            OR

a, b = list(map(lambda x: int(x), input().split()))
#이때, map()은 map(f, iterable)은 함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받는다.
#map은 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수이다.

#                            OR

xs = []  
for x in input().split():
xs.append(int(x))

a = xs[0]
b = xs[1]

#위 식들은 모두 같은 의미로 해석할 수 있다.

#카운터에 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전이 무한히 존재.
#손님에게 거슬러 줘야할 돈이 N원일 때 거슬러줘야 할 동전의 최소 개수는?
#단, 거슬러 줘야할 돈 N은 항상 10의 배수이다.
N = int(input())
count = 0
#가장 큰 단위인 500원부터 나누어준다.
coin = [500, 100, 50, 10]
for i in coin:
		count += N//coin
		N %= coin

print(count)

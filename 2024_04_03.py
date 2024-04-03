
# 백준 1436 영화감독 숌
# 솔루션 : result 값에 '666'이 포함하는지를 판단하여 
#'666'이 포함되어 있을 경우 cnt 변수를 1씩 증가

'''
n = int(input())
cnt = 0
result = 666

while True:
        if '666' in str(result):
                cnt += 1
        
        if n == cnt:
                break

        result += 1

print(result)

'''

# 백준 1676 팩토리얼 0의 개수


'''


n = int(input())
li = []
facto = 1

for i in range(n):
        facto = facto * n
        n = n -1


li = list(str(facto))
li = li[::-1]
answer = 0
for i in li:
        if i != '0':
                break
        if i == '0':
                answer += 1

print(answer)


'''


# 백준 7568 덩치
# 그리디 알고리즘?????
# 만일 자신보다 더 큰 덩치의 사람이 k명이라면 그 사람의 덩치 등수는 k+1
# 두 사람 A 와 B의 덩치가 각각 (x, y), (p, q)라고 할 때 
#x > p 그리고 y > q 이라면 우리는 A의 덩치가 B의 덩치보다 "더 크다"고 말한다


'''
n = int(input())
li = []
rank = []

for _ in range(n):
        mom, ki = map(int, input().split())
        li.append((mom, ki))

for i in range(n):
        cnt = 0
        for j in range(n):
                if li[i][0] < li[j][0] and li[i][1] < li[j][1]:
                        cnt += 1

        rank.append(cnt + 1)

for i in rank:
        print(i,end=" ")

'''




# 백준 11651 좌표 정렬하기 2


'''


n = int(input())
li = []

for i in range(n):
        x, y = map(int, input().split())
        li.append((x, y))


li.sort(key=lambda item: (item[1], item[0]))

for i in li:
        print(i[0], i[1])

# y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력


'''




# 백준 11650 좌표 정렬하기

# 좌표를 x좌표가 증가하는 순으로, 
# x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성


'''


n = int(input())
li = []

for i in range(n):
        x, y = map(int, input().split())
        li.append((x, y))

li.sort(key=lambda item: (item[0], item[1]))

for i in li:
        print(i[0], i[1])


'''




# 백준 11866 요세푸스 문제

'''


import sys
from collections import deque

li = []

n, k = map(int, input().split())

circle = list(range(1, n+1))

dq = deque(circle)


while dq:
        for _ in range(k-1):
                a = dq.popleft()
                dq.append(a)
        li.append(dq.popleft())

        if len(dq) == 1:
                li.append(dq[0])
                dq.popleft()





print("<", end="")
for i in range(n-1):
        print(li[i], end=", ")
print(li[n-1], end="")
print(">", end="")



'''































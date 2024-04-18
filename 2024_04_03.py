
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



# 백준 1920 수 찾기


'''

n = int(input())
li_a = list(map(int, input().split()))
m = int(input())
li_b = list(map(int, input().split()))

answer = []

for i in li_b:
        if i in li_a:
                answer.append(1)
        else:
                answer.append(0)

for i in answer:
        print(i)

'''

#-------------------------------------- 시간 초과 발생!!!!!!!!!!! -----------------------------------------------


'''



import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
a.sort() # 탐색의 대상인 리스트는 반드시 정렬을 해줘야 한다!!!!!

m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
# b 리스트는 탐색 대상이 아니므로 정렬을 해줄 필요가 없다!!!!


for i in b:
        left = 0
        right = n-1

        while left <= right:
                mid = (left + right) // 2
                if i > a[mid]:
                        left = mid + 1
                elif i < a[mid]:
                        right = mid - 1
                else:
                        left = mid
                        right = mid
                        break
        
        if left == mid and right == mid:
                print(1)
        else:
                print(0)

                

'''




# 백준 2164 카드2


'''


import sys
from collections import deque

n = int(input())
li = list(range(1, n+1))
dq = deque(li)

#print(len(dq))


while len(dq) > 1: # 조건을 그냥 while dq: 이렇게 쓰지 말 것!
        dq.popleft()
        dq.append(dq.popleft())  # 굳이 tmp 변수를 쓰지 말 것!

print(dq[0]) # while 문 안에서 지랄하지 말고 그냥 while 문 밖에서 하나 남은거 출력!



'''




# 백준 2839 설탕 배달


'''


n = int(input())
bong = 0

while n >= 0:
        if n % 5 == 0:
                bong += (n // 5)
                print(bong)
                break
        n -= 3
        bong += 1
else:
        print(-1)



'''




# 백준 9012 괄호
# 스택 자료구조 사용!!!


'''


t = int(input())

for i in range(t):
        stack = []
        target = input()

        for j in target:
                if j == '(':
                        stack.append(j)
                elif j == ')':
                        if len(stack) != 0: # 아까 집어넣은 ( 가 스택 안에 있다면
                                stack.pop() # ) 랑 스택 안에 있는 ( 가 1대1 대응으로 소멸!!!!
                        else:
                                print("NO")
                                break
        else:
                if len(stack) == 0:
                        print("YES")
                else:
                        print("NO")



'''



# 백준 18110 solved.ac


'''



import sys

def banoll(x):
        if x - int(x) >= 0.5:
                return int(x) + 1
        else:
                return int(x)



n = int(sys.stdin.readline())

if n:
        li = []

        for _ in range(n):
                li.append(int(sys.stdin.readline().strip()))
        
        cnt = banoll(n * 0.15)
        li.sort()

        if cnt > 0: # 제외되는 사람의 수가 1 이상
                print(banoll(sum(li[cnt:n-cnt])/len(li[cnt:n-cnt])))
        else: # 제외되는 사람의 수가 0 일때
                print(banoll(sum(li)/len(li)))
else: # 투표가 0일 때
        print(0)
        



'''




'''


# 프로그래머스
# 게임 맵 최단거리


import sys
from collections import deque

def solution(maps):
    # 상, 하, 좌, 우 이동 방향을 정의합니다.
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 맵의 행과 열의 개수를 구합니다.
    n = len(maps)  # 행의 개수
    m = len(maps[0])  # 열의 개수

    # 방문 여부를 기록하는 2차원 배열을 생성합니다.
    visited = [[False] * m for _ in range(n)]

    # BFS를 위한 큐를 생성하고, 시작 지점을 큐에 추가합니다.
    q = deque()
    q.append((0, 0))  # 시작 지점 (0, 0)

    # 시작 지점을 방문했음을 표시합니다.
    visited[0][0] = True

    # BFS를 수행합니다.
    while q:
        # 큐에서 현재 위치를 꺼냅니다.
        y, x = q.popleft()
        
        # 현재 위치에서 상하좌우로 이동합니다.
        for i in range(4):
            nx = x + dx[i]  # 다음 열
            ny = y + dy[i]  # 다음 행

            # 다음 위치가 맵의 범위 내에 있고, 갈 수 있는 길(1)인 경우를 확인합니다.
            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] == 1:
                # 다음 위치를 방문하지 않았다면 방문 표시하고 큐에 추가합니다.
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny, nx))
                    # 다음 위치까지의 거리를 현재 위치에서의 거리 + 1로 업데이트합니다.
                    maps[ny][nx] = maps[y][x] + 1

    # 상대 팀 진영까지의 거리가 1인 경우, 즉 도달할 수 없는 경우 -1을 반환합니다.
    if maps[n - 1][m - 1] == 1:
        return -1
    # 그렇지 않은 경우, 상대 팀 진영까지의 최소 이동 거리를 반환합니다.
    else:
        return maps[n - 1][m - 1]





import sys
from collections import deque

def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    n = len(maps)
    m = len(maps[0])

    visited = [[False]*m for _ in range(n)]

    q = deque()
    q.append((0, 0))

    visited[0][0] = 1

    while q:
        y, x = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] == 1:
                        if not visited[ny][nx]:
                                visited[ny][nx] = True
                                q.append((ny, nx))
                                maps[ny][nx] = maps[y][x] + 1
    if maps[n - 1][m - 1] == 1:
        return -1
    else:
        return maps[n-1][m-1]





'''






# 회문 문자열 검사
import sys
#sys.stdin=open("input.txt", "r")  # 파일에서 입력을 받을 경우를 위해 사용되는 코드입니다. 여기서는 주석 처리되어 있습니다.

n = int(input())  # 첫 줄에서 회문 검사를 할 문자열의 개수를 입력 받습니다.

for i in range(1, n+1):  # n번 반복합니다. 각각의 반복에서는 새로운 문자열을 처리합니다.
    str_input = input()  # 문자열을 입력 받습니다.
    str_input = str_input.upper()  # 입력 받은 문자열을 모두 대문자로 변환합니다. (대소문자를 구분하지 않기 때문에)

    for j in range(len(str_input)//2):  # 문자열의 반만큼 반복합니다. 회문을 검사할 때는 문자열의 반만 확인하면 됩니다.
        if str_input[j] != str_input[-1-j]:  # 문자열의 처음과 끝을 비교하여 다른 경우,
            print("#%d NO" % i)  # 해당 문자열은 회문이 아니므로 NO를 출력하고
            break  # 반복문을 빠져나갑니다.
    else:  # 반복문이 중간에 중단되지 않고 모두 통과했을 경우
        print("#%d YES" % i)  # 해당 문자열은 회문이므로 YES를 출력합니다.








# 숫자만 추출
import sys
#sys.stdin=open("input.txt", "r")  # 파일에서 입력을 받을 경우를 위해 사용되는 코드입니다. 여기서는 주석 처리되어 있습니다.

s = input()  # 문자열을 입력 받습니다.
res = 0  # 추출된 숫자들로 만들어진 자연수를 저장할 변수를 초기화합니다.

# 문자열을 순회하면서 숫자를 추출하여 자연수를 만듭니다.
for x in s:
    if x.isdecimal():  # 만약 현재 문자가 숫자라면
        res = res * 10 + int(x)  # 해당 숫자를 추출하여 res에 자릿수를 늘려가며 자연수를 만듭니다.

print(res)  # 만들어진 자연수를 출력합니다.

cnt = 0  # 약수의 개수를 저장할 변수를 초기화합니다.

# 1부터 자연수까지 반복하면서 약수의 개수를 찾습니다.
for i in range(1, res + 1):
    if res % i == 0:  # 현재 숫자가 자연수의 약수인 경우
        cnt += 1  # 약수의 개수를 증가시킵니다.

print(cnt)  # 약수의 개수를 출력합니다.









# 카드 역배치

import sys
#sys.stdin=open("input.txt", "r")  # 파일에서 입력을 받을 경우를 위해 사용되는 코드입니다. 여기서는 주석 처리되어 있습니다.

a = list(range(21))  # 1부터 20까지의 숫자를 리스트에 저장합니다.

for _ in range(10):  # 구간이 10개 주어지므로 10번 반복합니다.
    s, e = map(int, input().split())  # 구간의 시작과 끝을 입력 받습니다.
    for i in range((e - s + 1) // 2):  # 구간을 반으로 나누어서 반복합니다.
        a[s + i], a[e - i] = a[e - i], a[s + i]  # 시작과 끝을 서로 바꿔줍니다. (역순으로 뒤집는 과정)
        
a.pop(0)  # 리스트에서 첫 번째 요소를 삭제합니다. (0은 사용하지 않으므로)
for x in a:  # 리스트에 있는 요소들을 순회하며 출력합니다.
    print(x, end=' ')  # 한 줄에 하나씩 출력하고 공백을 추가합니다.










# 두 리스트 합치기
import sys
#sys.stdin=open("input.txt", "r")  # 파일에서 입력을 받을 경우를 위해 사용되는 코드입니다. 여기서는 주석 처리되어 있습니다.

n = int(input())  # 첫 번째 리스트의 길이를 입력 받습니다.
a = list(map(int, input().split()))  # 첫 번째 리스트를 입력 받습니다.
m = int(input())  # 두 번째 리스트의 길이를 입력 받습니다.
b = list(map(int, input().split()))  # 두 번째 리스트를 입력 받습니다.

p1 = p2 = 0  # 각 리스트를 순회할 인덱스를 초기화합니다.
c = []  # 두 리스트를 합친 결과를 저장할 리스트를 초기화합니다.

# 두 리스트를 합치는 과정입니다.
while p1 < n and p2 < m:  # 두 리스트 중 하나라도 모두 순회할 때까지 반복합니다.
    if a[p1] < b[p2]:  # 첫 번째 리스트의 현재 요소가 두 번째 리스트의 현재 요소보다 작을 때
        c.append(a[p1])  # 첫 번째 리스트의 현재 요소를 결과 리스트에 추가하고
        p1 += 1  # 첫 번째 리스트의 다음 요소로 이동합니다.
    else:  # 두 번째 리스트의 현재 요소가 첫 번째 리스트의 현재 요소보다 작거나 같을 때
        c.append(b[p2])  # 두 번째 리스트의 현재 요소를 결과 리스트에 추가하고
        p2 += 1  # 두 번째 리스트의 다음 요소로 이동합니다.

# 남은 요소들을 결과 리스트에 추가하는 과정입니다.
if p1 < n:  # 첫 번째 리스트에 남은 요소가 있는 경우
    c += a[p1:]  # 첫 번째 리스트의 남은 요소들을 결과 리스트에 추가합니다.
if p2 < m:  # 두 번째 리스트에 남은 요소가 있는 경우
    c += b[p2:]  # 두 번째 리스트의 남은 요소들을 결과 리스트에 추가합니다.

# 결과 리스트를 출력합니다.
for x in c:
    print(x, end=' ')










# 수들의 합


import sys
#sys.stdin = open("input.txt", 'r')  # 파일에서 입력을 받을 경우를 위해 사용되는 코드입니다. 여기서는 주석 처리되어 있습니다.

n, m = map(int, input().split())  # 수열의 길이 N과 합 M을 입력 받습니다.
a = list(map(int, input().split()))  # N개의 수로 된 수열을 입력 받습니다.

lt = 0  # 수열의 시작 인덱스를 가리키는 포인터를 초기화합니다.
rt = 1  # 수열의 끝 인덱스를 가리키는 포인터를 초기화합니다.
tot = a[0]  # 현재 부분 수열의 합을 저장하는 변수를 초기화합니다.
cnt = 0  # 합이 M이 되는 경우의 수를 저장하는 변수를 초기화합니다.

while True:
    if tot < m:  # 현재 부분 수열의 합이 M보다 작은 경우
        if rt < n:  # 수열의 끝 인덱스가 수열의 길이를 넘어가지 않으면
            tot += a[rt]  # 수열의 끝 인덱스를 오른쪽으로 한 칸 이동하고 합을 업데이트합니다.
            rt += 1
        else:  # 수열의 끝 인덱스가 수열의 길이를 넘어가는 경우
            break  # 반복문을 종료합니다.
    elif tot == m:  # 현재 부분 수열의 합이 M과 같은 경우
        cnt += 1  # 경우의 수를 증가시키고
        tot -= a[lt]  # 수열의 시작 인덱스를 오른쪽으로 한 칸 이동하고 해당 요소를 합에서 빼줍니다.
        lt += 1
    else:  # 현재 부분 수열의 합이 M보다 큰 경우
        tot -= a[lt]  # 수열의 시작 인덱스를 오른쪽으로 한 칸 이동하고 해당 요소를 합에서 빼줍니다.
        lt += 1

print(cnt)  # 경우의 수를 출력합니다.








# 격자판 최대합










# 사과나무(다이아몬드)










#곳감(모래시계)













# 봉우리












# 스토쿠 검사















# 격자판 회문수










# 이분검색












# 랜선짜르기(결정 알고리즘)










# 뮤직비디오(결정알고리즘)
















# 마구간 정하기(결정알고리즘)















# 회의실 배정(그리디)















# 씨름 선수(그리디)















# 창고 정리
















# 침몰하는 타이타닉(그리디)



















# 증가수열 만들기(그리디)


















# 역수열(그리디)














# 가장 큰 수













# 쇠막대기















# 후위 표기식 만들기














# 후위식 연산














# 공주 구하기(큐 자료구조 사용)
















# 응급실

















# 교육과정 설계












# 단어 찾기














# 아나그램















# 최소힙












# 최대힙













# 재귀함수를 이용한 이진수 출력
















# 이진트리 순회(깊이 우선 탐색)



















# 부분집합 구하기(DFS)

















# 합이 같은 부분집합(DFS)














# 바둑이 승차(DFS)























# 중복순열 구하기
















# 동전 교환


















# 순열 구하기

















# 수열 추측하기















# 조합 구하기















# 수들의 조합
















# 인접행렬(가중치 방향그래프)

















# 경로 탐색(그래프 DFS)










# 최대점수 구하기(DFS)











# 휴가












# 양팔저울(DFS)














# 동전 바꿔주기(DFS)










# 동전 분배하기(DFS)











# 알파코드(DFS)











# 송아지 찾기(BFS)















# 사과나무(BFS)















# 미로의 최단거리 통로(BFS)













# 미로탐색(DFS)










# 등산경로(DFS)















# 단지 번호 붙이기(DFS, BFS)










# 섬나라 아일랜드(BFS)












# 안전영역(BFS)









# 토마토(BFS)










# 사다리 타기(DFS)











# 피자 배달 거리














# 네트워크 선 자르기(바텀업)









# 네트워크 선 자르기(탑 다운)














# 계단오르기(탑 다운)












# 계단오르기(바텀 업)












# 최대 부분 증가수열









# 최대 선 연결하기











# 가장 높은 탑 쌓기













# 알리바바와 40인의 도둑(바텀 업)















# 알리바바와 40인의 도둑(탑 다운)










# 가방문제(냅색)




















# 동전교환
















# 최대 점수 구하기(냅색)

















# 도시 이동(플로이드 워샬)




















# 회장뽑기(플로이드 워샬)
























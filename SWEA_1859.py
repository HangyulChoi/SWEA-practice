"""
@author: choihangyul
SWEA 1859. 백만 장자 프로젝트
"""
t = int(input())
def solve(arr):
    arr =  arr[::-1] # 거꾸로 뒤집기 
    m = arr[0]
    ans = 0
    for i in range(1, len(arr)):
        if m > arr[i]:
            ans += m - arr[i]
        else:
            m = arr[i]
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print('#{} {}'.format(i, solve(arr)))

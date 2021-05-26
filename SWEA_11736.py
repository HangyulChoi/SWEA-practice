"""
@author: choihangyul
SWEA 11736. 평범한 숫자
"""

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    for i in range(1, n-1):
        tmp = arr[i]
        arr_n =  sorted(arr[i-1:i+2])
        if tmp == arr_n[1]:
            ans += 1

    print('#{} {}'.format(test_case, ans))
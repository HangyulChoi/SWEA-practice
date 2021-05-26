"""
@author: choihangyul
SWEA 1206. View
"""

for test_case in range(1, 11):
    ans = 0
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(2, n-1):
        if (arr[i] < arr[i-1]) or (arr[i] < arr[i-2]) or (arr[i]<arr[i+1]) or (arr[i]<arr[i+2]):
            continue
        else:
            ans += arr[i] - max(arr[i-2], arr[i-1], arr[i+1], arr[i+2])
            
    print('#{} {}'.format(test_case, ans))
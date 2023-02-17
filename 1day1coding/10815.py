#10815번
from sys import stdin

count1 = int(stdin.readline())
card = list(map(int,stdin.readline().split()))
card.sort()
count2 = int(stdin.readline())
check = list(map(int,stdin.readline().split()))

for i in check:
    start = 0
    end = count1
    mid = (start + end) // 2
    while 1:
        
        if i == card[mid]:
            print("1", end=' ')
            break
        elif i > card[mid]:
            start = mid
        elif i < card[mid]:
            end = mid
        mid = (start + end) // 2
        
        if (start >= mid or end <= mid) and i != card[mid]:
            print("0", end=' ')
            break

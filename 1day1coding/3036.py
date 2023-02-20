#3036

from sys import stdin

count = int(stdin.readline())

r_list = list(map(int,stdin.readline().split()))

for i in range(1,len(r_list)):
    if r_list[0] % r_list[i] == 0:
        print(r_list[0]//r_list[i],end='')
        print("/",end='')
        print("1")
    else:
        print(r_list[0] - r_list[i] * (r_list[0] // r_list[i]),end='')
        print("/",end='')
        print(r_list[0] % r_list[i])
    
    
def gcd(a, b):
    while(b != 0):
        n = a%b
        a = b
        b = n
    return a

n = int(input())
li = list(map(int, input().split()))
for i in range(1, n):
    g = gcd(li[0], li[i])
    print('{0}/{1}'.format(li[0]//g, li[i]//g))

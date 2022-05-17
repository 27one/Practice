N = int(input())
num = list(map(int,input().split()))
def isPrime(n):
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False
cnt = 0
for i in range(N):
    
    if isPrime(num[i]):
        cnt += 1
print(cnt)


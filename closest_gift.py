#defining prime function
def prime(n):
    a=0
    if n==1 or n==0:
        return False
    for i in range(2,int(n**(1/2)+1)):
        if n%i==0:
            a+=1
    return a==0

# taking in current position
curr=int(input())
steps=0
while not prime(curr):
    steps+=1
    curr+=1

print(f'Distance from the closest gift: {steps}')

a=input().split()
n=len(a)
b=['*']*(2*n)
print(*a)
for i in range(1,n):
    print(*a[:(n-i)],*b[:(2*i-1)])
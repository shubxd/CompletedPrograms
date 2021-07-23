
#using ASCII values to sort the arrays
def maxnum(arr):
    arr=list(map(str,arr))
    arr.sort(reverse=True)
    print(''.join(arr))

arr=list((map(int,input().split())))

maxnum(arr)


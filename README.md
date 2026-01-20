# LONGEST SUBARRAY /SUBSTRING WHERE <CONDITION>
# LONGEST SUBARRAY WHERE SUM<given value k
# expand->with right pointer shrink->left pointer
arr=list(map(int,input().split()))
k=int(input())
left=0
right=0
n=len(arr)
Sum=0
maxlen=0
while(right<n):#O(N)
    Sum+=arr[right]
    while(Sum>k):#O(SUM)
        Sum-=arr[left]
        left+=1
    maxlen=max(maxlen,right-left+1)
    right+=1
print(maxlen)
#   output:2 5 1 10 10
#          14
#          3

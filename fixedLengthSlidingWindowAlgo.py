def fixedLengthSubArray(arr,k):
    sum=0
    for i in range(k):
        sum=sum+arr[i]
    r=k-1
    l=0
    maxSum=sum
    while(r<len(arr)-1):
        sum=sum-arr[l]
        l=l+1
        r=r+1
        sum=sum+arr[r] 
        maxSum=max(sum,maxSum)
    return maxSum
if __name__=="__main__":
    arr=[2,3,-8,7,-1,2,3]
    k=3
    print(fixedLengthSubArray(arr,k))
t = int(input())

while t > 0:
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    t -= 1
    # Your code goes here
    temp=0 #To calculate the price after every item after reducing y
    totSum=sum(a) # sum of array
    for i in a:
        if (y>i):
            pass # Since i's value is considered Zero no need to add
        else:
            temp2=i-y # for subtracted value of y from list element
            temp=temp+temp2
    discountSum=temp+x # sum of discounted price and discount COUPON
    if totSum>discountSum:
        print("COUPON")
    else :
        print("NO COUPON")
            

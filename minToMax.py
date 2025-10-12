t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    # Your code goes here
    a_min=min(a)
    cnt=0
    for i in a:
        if i>a_min:
            cnt=cnt+1
            
    print(cnt)
    t -= 1
    

# Read the number of test cases
t = int(input())

# Process each test case
while t > 0:
    # Read the size of the array
    n = int(input())
    
    # Read the array elements as strings and convert them to integers
    arr = input().split()
    for i in range(n):
        arr[i] = int(arr[i])
    
    # Find and print the maximum element in the array
    print(max(arr))
    
    # Decrement the test case counter
    t = t - 1

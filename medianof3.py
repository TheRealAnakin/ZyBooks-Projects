



def main():
    x = int(input())
    y = int(input())
    z = int(input())
    arr = [x,y,z]
    
    for i in range(0, len(arr) - 1):
        if arr[i] > arr[i + 1]:
            biggest = arr[i]
    if z > x:
        if z > y:
            biggest = z
    if x > z:
        if x > y:
            biggest = x
    if y > x:
        if y > z:
            biggest = y
    if x < z:
        if x < y:
            smallest = x
    if z < y:
        if z < x:
            smallest = z
    if y < x:
        if y < z:
            smallest = y
    for i in range(0, len(arr) - 1):
        if arr[i] != biggest:
            if arr[i] != smallest:
                median = arr[i]
    if arr[len(arr) - 1] != biggest:
        if arr[len(arr)-1] != smallest:
            median = arr[len(arr)-1]
    print(median)
main()

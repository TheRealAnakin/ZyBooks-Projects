def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    arr = [a,b,c,d]
    
    n = 0

    for i in range(0, len(arr) - 1):
        if arr[i] % 2 == 1:
            n = n + 1
    if arr[len(arr) - 1] % 2 == 1:
        n = n + 1
    print(n)



main()

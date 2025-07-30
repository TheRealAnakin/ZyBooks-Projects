def main():
    x = int(input())
    y = int(input())
    z = int(input())
    max = 0
    arr = [x,y,z]
    for i in range(0,len(arr) - 1):
        if arr[len(arr) - 1] > arr[i]:
            max = arr[len(arr) -1]
        if arr[i] > arr[i + 1]:
            max = arr[i]

    print(f"Max of {arr} is {max}")

main()





def main():
    x = int(input())
    y = int(input())
    z = int(input())
    arr = [x,y,z]
    
    for i in range(0, len(arr) - 1):
        if arr[i] > arr[i + 1]:
            biggest = arr[i]
        
        
    print("Biggest:", biggest)
main()

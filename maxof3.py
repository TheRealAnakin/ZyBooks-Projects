def main():
    x = int(input())
    y = int(input())
    z = int(input())
    max = 0
    arr = [x,y,z]
    if x > y > z:
        max = x
    elif y > x > z:
        max = y
    else:
        max = z
    print(f"Max of {arr} is {max}")

main()

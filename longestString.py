


def main():
    a = str(input())
    b = str(input())
    if len(a) > len(b):
        print(f"{a} is longer than {b}")
    elif len(b) > len(a):
        print(f"{b} is longer than {a}")
    else:
        print(f"{a} and {b} are the same length")

main()

def main():
    number = str(input())
    split = number.split()
    digits = len([int(d) for d in number])
    if digits > 1:
        print(digits, "digits")
    else:
        print(digits, "digit")
main()


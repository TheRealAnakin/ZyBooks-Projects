def main():
    phraseOne = str(input())
    phraseTwo = str(input())
    if phraseOne == phraseTwo:
        print("Both phrases match")
        quit()
    if phraseOne in phraseTwo:
        print(f"{phraseOne} is found within {phraseTwo}")
    elif phraseTwo in phraseOne:
        print(f"{phraseTwo} is found within {phraseOne}")
    elif phraseOne == phraseTwo:
        print("Both phrases match")
    else:
        print("No matches")

main()

def coinValue(total):
    dollars = 0
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0
    if total / 100 != 0:



def main():
    total = int(input())
    if total <= 0:
        print("No change")
    else:
        coinValue(total)

main()

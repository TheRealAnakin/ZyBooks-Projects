def coinValue(total):
    dollars = 0
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0
    if total // 100 != 0:
        dollars = total // 100
        total = total - (dollars * 100)
        if dollars > 1:
            print(dollars, "Dollars")
        else:
            print(dollars, "Dollar")
        if total // 25 != 0:
            quarters = total // 25
            total = total - (quarters * 25)
            if quarters > 1:
                print(quarters, "Quarters")
            else:
                print(quarters, "Quarter")
        if total // 10 !=0:
            dimes = total // 10
            total = total - (dimes * 10)
            if dimes > 1:
                print(dimes, "Dimes")
            else:
                print(dimes, "Dime")
        if total // 5 != 0:
            nickels = total // 5
            total = total - (nickels * 5)
            if nickels > 1:
                print(nickels, "Nickels")
            else:
                print(nickels, "Nickel")
        if total // 1 != 0:
            pennies = total // 1 
            total = total - (pennies * 1)
            if pennies > 1:
                print(pennies, "Pennies")
            else:
                print(pennies, "Pennie")
    elif total // 25 != 0:
        quarters = total // 25
        total = total - (quarters * 25)
        if quarters > 1:
            print(quarters, "Quarters")
        else:
            print(quarters, "Quarter")
        if total // 10 !=0:
            dimes = total // 10
            total = total - (dimes * 10)
            if dimes > 1:
                print(dimes, "Dimes")
            else:
                print(dimes, "Dime")
        if total // 5 != 0:
            nickels = total // 5
            total = total - (nickels * 5)
            if nickels > 1:
                print(nickels, "Nickels")
            else:
                print(nickels, "Nickel")
        if total // 1 != 0:
            pennies = total // 1 
            total = total - (pennies * 1)
            if pennies > 1:
                print(pennies, "Pennies")
            else:
                print(pennies, "Pennie")
    elif total // 10 !=0:
        dimes = total // 10
        total = total - (dimes * 10)
        if dimes > 1:
            print(dimes, "Dimes")
        else:
            print(dimes, "Dime")
        if total // 5 != 0:
            nickels = total // 5
            total = total - (nickels * 5)
            if nickels > 1:
                print(nickels, "Nickels")
            else:
                print(nickels, "Nickel")
        if total // 1 != 0:
            pennies = total // 1 
            total = total - (pennies * 1)
            if pennies > 1:
                print(pennies, "Pennies")
            else:
                print(pennies, "Pennie")
    elif total // 5 !=0:
        nickels = total // 5
        total = total - (nickels * 5)
        if nickels > 1:
            print(nickels, "Nickels")
        else:
            print(nickels, "Nickel")
        if total // 1 != 0:
            pennies = total // 1 
            total = total - (pennies * 1)
            if pennies > 1:
                print(pennies, "Pennies")
            else:
                print(pennies, "Pennie")
    elif total // 1 !=0:
        pennies = total // 1 
        total = total - (pennies * 1)
        if pennies > 1:
            print(pennies, "Pennies")
        else:
            print(pennies, "Pennie")

        
def main():
    total = int(input())
    if total <= 0:
        print("No change")
    else:
        coinValue(total)

main()

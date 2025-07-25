import math




def main():
    year = int(input())
    if year % 4 == 0:
        if abs(year) % 100 == 00:
            if year % 400 == 0:
                print(year, "- leap year")
            else:
                print(year, "- not a leap year")
        else:
            print(year, "- leap year")
     
    else:
        print(year, "- not a leap year")




main()

months = ['January', 'Feburary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

spring = ['Feburary', 'March', 'April', 'May', 'June']
summer = ['June', 'July', 'August', 'September']
autumn = ['September', 'October', 'November', 'December']
winter = ['December', 'January', 'Feburary', 'March']



def valid(month, day):
    if month in months and 0 < day < 31:
        return True
    else:
        return False

def deduceSeason(month, day):
    #spring
    if month in spring:
        if month == "June" and day > 20:
            print("Invalid")
        elif month == "March" and day < 20:
            print("Invalid")
        else:
            print("Spring")
    #summer
    if month in summer:
        if month == "June" and day > 21:
            print("Invalid")
        elif month == "September" and day > 21:
            print("Invalid")
        else:
            print("Summer")
     #autumn
    if month in autumn:
        if month == "September" and day < 22:
            print("Invalid")
        elif month == "December" and day > 20:
            print("Invalid")
        else:
            print("Autumn")
def main():
    month = str(input())
    day = int(input())
    if valid(month, day):
        deduceSeason(month, day)
    else:
        print("Invalid")


main()

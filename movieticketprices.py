def main():
    timePeriod = str(input())
    age = int(input())
    if age < 4:
        print("free")
    if timePeriod == "day":
        if age >= 4:
            print("$8")
    if timePeriod == "night":
        if 3 < age < 17:
            print("$12")
        if 16 < age < 55:
            print("$15")
        if age >= 55:
            print("$13")



main()


def main():
    service =   str(input("Enter desired auto service:\n"))
    if service == "Oil change":
        print("You entered:", service)
        print(f"Cost of {service.lower()}: $35")
    elif service == "Tire rotation":
        print("You entered:", service)
        print(f"Cost of {service.lower()}: $19")
    elif service == "Car wash":
        print("You entered:", service)
        print(f"Cost of {service.lower()}: $7")
    else:
        print("You entered:", service)
        print("Error: Requested service is not recognized")


main()

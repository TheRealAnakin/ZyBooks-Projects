def printBullshit():
    print("""Davy's auto shop services
Oil change -- $35
Tire rotation -- $19
Car wash -- $7
Car wax -- $12""")
    print()


def printInvoice(service1, service2):
    price = 0
    if service1 == "Oil change":
        output1 = "Oil change, $35"
        price = price + 35
    elif service1 == "Tire rotation":
        output1 = "Tire rotation, $19"
        price = price + 19
    elif service1 == "Car wash":
        output1 = "Car wash, $7"
        price = price + 7
    elif service1 == "Car wax":
        output1 = "Car wax, $12"
        price = price + 12
    else:
        output1 = "No service"


    if service2 == "Oil change":
        output2 = "Oil Change, $35"
        price = price + 35
    elif service2 == "Tire rotation":
        output2 = "Tire rotation, $19"
        price = price + 19
    elif service2 == "Car wash":
        output2 = "Car wash, $7"
        price = price + 7
    elif service2 == "Car wax":
        output2 = "Car wax, $12"
        price = price + 12
    else:
        output2 = "No service"
    print("Davy's auto shop invoice")
    print()
    print(f"Service 1: {output1}")
    print(f"Service 2: {output2}")
    print()
    print(f"Total: ${price}")



def main():
    printBullshit()
    firstService = str(input("Select first service:\n"))
    secondService = str(input("Select second service:\n"))
    print()
    printInvoice(firstService, secondService)


main()

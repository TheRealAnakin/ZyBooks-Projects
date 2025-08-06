def main():
    speedLimit = int(input())
    mph = int(input())
    ticket = 0
    if mph <= speedLimit - 10:
        ticket = ticket + 50
    lower = speedLimit + 6
    higher = speedLimit + 20
    if lower <= mph <= higher:
        ticket = ticket + 75
    lo = speedLimit + 21
    hi = speedLimit + 40
    if lo <= mph <= hi:
        ticket = ticket + 150
    if mph > speedLimit + 40:
        ticket = ticket + 300
    print(ticket)




main()

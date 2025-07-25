def getScoreName(strokes, par):

    if strokes == par - 2:
        return "Eagle"
    elif strokes == par - 1:
        return "Birdie"
    elif strokes == par:
        return "Par"
    elif strokes == par + 1 and strokes != 2:
        return "Bogey"
    else:
        return "Error"
    if par == 1 and strokes == 2:
        return "Error"









def main():
    strokes = int(input())
    par = int(input())
    scoresName = getScoreName(strokes, par)
    print(f"Par {par} in {strokes} strokes is {scoresName}")


main()






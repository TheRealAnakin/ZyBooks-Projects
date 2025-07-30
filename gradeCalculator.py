def parseInformation():
    global studentStatus
    studentStatus = str(input())
    if studentStatus in ("UG", "G", "DL"):
        numbers = str(input())
        nums = numbers.split()
        return nums
    else:
        print("Error: student status must be UG, G or DL")
        quit()



def calculateAverages(homeworkPoints, quizPoints, midtermExamScore, finalExamScore):
    homeworkPoints = float(homeworkPoints) / 800 * 100
    quizPoints = float(quizPoints) / 400 * 100
    midtermExamScore = float(midtermExamScore) / 150 * 100
    finalExamScore = float(finalExamScore) / 200 * 100
    return [homeworkPoints, quizPoints, midtermExamScore, finalExamScore]


def main():
    nums = parseInformation()
    homeworkPoints = nums[0]
    quizPoints = nums[1]
    midtermExamScore = nums[2]
    finalExamScore = nums[3]
    averages = calculateAverages(homeworkPoints, quizPoints, midtermExamScore, finalExamScore)
    for i in range(0, len(averages)):
        if averages[i] > 100:
            averages[i] = 100
    print(f"Homework: {averages[0]:2.1f}%")
    print(f"Quizzes: {averages[1]:2.1f}%")
    print(f"Midterm: {averages[2]:2.1f}%")
    print(f"Final Exam: {averages[3]:2.1f}%")


main()

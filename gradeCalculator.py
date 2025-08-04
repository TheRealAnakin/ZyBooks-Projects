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

def findOutGrade(gAverage):
    if gAverage >= 90:
        grade = "A"
    elif 79 < gAverage < 89:
        grade = "B"  
    elif 69 < gAverage < 79:
        grade = "C"   
    elif 60 < gAverage < 69:
        grade = "D"   
    elif gAverage < 60:
        grade = "F"
    return grade

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
    if studentStatus == "UG":
        gAverage = (averages[0] * 0.20) + (averages[1] * 0.20) + (averages[2] * 0.30) + (averages[3] * 0.30)
    elif studentStatus == "G":
        gAverage = (averages[0] * 0.15) + (averages[1] * 0.05) + (averages[2] * 0.35) + (averages[3] * 0.45)
    else:
        gAverage = (averages[0] * 0.05) + (averages[1] * 0.05) + (averages[2] * 0.40) + (averages[3] * 0.50)
    print(f"{studentStatus} average: {gAverage:2.1f}%")
    grade = findOutGrade(gAverage)
    print(f"Course grade: {grade}")
main()

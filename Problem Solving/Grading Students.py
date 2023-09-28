def gradingStudents(grades):
    ans = []
    for i in range(len(grades)):
        if ((math.ceil(grades[i] / 5) * 5) - grades[i] < 3 and grades[i] >= 38):
            ans.append(math.ceil(grades[i] / 5) * 5)
        else:
            ans.append(grades[i])
    return ans

import random

def cal_game():
    i = 1
    correctCount = 0
    reports = ""
    while i <= 5:
        n1 = random.randint(1, 51)
        n2 = random.randint(1, 11)
        if n2 > n1:
            temp = n1
            n1 = n2
            n2 = temp

        print("what is {} - {} ? ".format(n1, n2))
        ans = int(input())
        if (n1 - n2) == ans:
            print("your answer is correct!")
            correctCount += 1
        else:
            print("your answer is wrong.")
            print(n1, " - ", n2, "should be ", (n1 - n2))
        i += 1
        reports += "\n" + str(n1) + "-" + str(n2) + "=" + str(ans) + ("  correct" if (n1 - n2 == ans) else "  wrong")
    print("\ncorrect count is {}".format(correctCount))
    print(reports)

# cal_game()
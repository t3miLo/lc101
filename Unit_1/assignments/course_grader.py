# Write a course_grader function that takes a list of test scores as its parameter.
# It will add up these test scores and calculate an average score.
# It should then return a message of "pass" or "fail" depending on these two conditions:
#       -If the average score is greater than or equal to 70 and no single test score is
#           below 50, then return a message of "pass".
#       -If the average score is lower than 70 or at least one test score is below 50,
#           then return a message of "fail".


def course_grader(test_scores):
    # Your code here
    avg = int(sum(test_scores) / float(len(test_scores)))
    if min(test_scores) < 50 or avg < 70:
        return "fail"
    elif avg >= 70 and min(test_scores) != 50:
        return "pass"


def main():
    print(course_grader([100, 75, 45]))     # "fail"
    print(course_grader([100, 70, 85]))     # "pass"
    print(course_grader([80, 60, 60]))      # "fail"
    print(course_grader([80, 80, 90, 30, 80]))  # "fail"
    print(course_grader([70, 70, 70, 70, 70]))  # "pass"


if __name__ == "__main__":
    main()

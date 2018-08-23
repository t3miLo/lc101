# Write a program that will function as a grade book,
# allowing a user (a professor or teacher) to enter the class roster for a course,
# along with each student’s cumulative grade. It then prints the class roster along
# with the average cumulative grade. Grades are on a 0-100 percentage scale.
# Use 2 lists (grades and students) and the enumerate function in your solution.


def main():
    roster = input('Input the student names for the class roster with a space only!:')
    roster_split = roster.split()
    grades = input(
        'Input the grades for each student in the same order as when you inputed the name!:')
    grade_split = grades.split()
    roster_class = {}

    counter = 0

    for name in roster_split:
        roster_class[name] = grade_split[counter]
        counter += 1

    print('Class Roster:')
    for key in roster_class:
        print('%s %d' % (key, roster_class[key])


if __name__ == '__main__':
    main()

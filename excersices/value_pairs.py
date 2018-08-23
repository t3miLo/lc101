# Write a program that allows the user to enter a string.
# It then prints a table of the letters of the alphabet in alphabetical
# order which occur in the string together with the number of times each letter occurs.
# Case should be ignored


def main():
    dict = {}
    string = input('Please enter a sentence: ')
    string_lower = string.lower()

    for letter in string_lower:
        if letter.isalpha():

            if letter not in dict:
                dict[letter] = string.count(letter)

    for key in sorted(dict.keys()):
        print("%s: %s" % (key, dict[key]))


if __name__ == '__main__':
    main()

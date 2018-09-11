# Write a function analyze_text that receives a string as input.
# Your function should count the number of alphabetic characters
# (a through z, or A through Z) in the text and also keep track of
# how many are the letter 'e' (upper or lowercase).

# Your function should return an analysis of the text in the
# form of a string phrased exactly like this:

# “The text contains 240 alphabetic characters, of which 105 (43.75%) are ‘e’.”


def analyze_text(text):
    # Your code here
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    e = 'e'
    length = 0
    for each_char in text:
        if each_char.lower() in alpha:
            length += 1
    total = 0

    for each_char in text:
        if each_char.lower() == e:
            total += 1
    percent = (total / length) * 100

    answer = "The text contains {} alphabetic characters, of which {} ({}%) are 'e'."
    return answer.format(length, total, percent)


# Tests 4-6: solutions using str.format should pass these
text4 = "Eeeee"
answer4 = "The text contains 5 alphabetic characters, of which 5 (100%) are 'e'."
print(analyze_text(text4))
print(answer4)

text5 = "Blueberries are tasteee!"
answer5 = "The text contains 21 alphabetic characters, of which 7 (33.33333333333333%) are 'e'."
print(analyze_text(text5))
print(answer5)

text6 = "Wright's book, Gadsby, contains a total of 0 of that most common symbol ;)"
answer6 = "The text contains 55 alphabetic characters, of which 0 (0%) are 'e'."
print(analyze_text(text6))
print(answer6)

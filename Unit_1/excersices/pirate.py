import re


def main():

    pirate_words = {
        'sir': 'matey',
        'hotel': 'fleabag inn',
        'student': 'swabbie',
        'boy': 'matey',
        'madam': 'proud beauty',
        'professor': 'foul blaggart',
        'restaurant': 'galley',
        'your': 'yer',
        'excuse': 'arr',
        'students': 'swabbies',
        'are': 'be',
        'lawyer': 'foul blaggart',
        'restroom'	: "th'head",
        'my': 'me',
        'hello': 'avast',
        'is': 'be',
        'man': 'matey',
    }
    text = "hello my man, please excuse your professor to the restroom!"
    text_split = re.findall(r"[\w']+", text)
    pirate_text = text
    pirate_text = pirate_text.replace('the ', '')

    for each_word in text_split:

        if each_word in pirate_words:

            pirate_text = pirate_text.replace(each_word, pirate_words.get(each_word))

    print(pirate_text)


if __name__ == '__main__':
    main()

def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    # TODO your code here
    names = fullname.split(' ')
    initials = ''
    for name in names:
        initials += name[0].upper()

    return initials


def main():
    user = input('What is your name?\n')
    print(get_initials(user))


if __name__ == '__main__':
    main()

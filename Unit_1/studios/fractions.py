# Fraction
# A fraction has a numerator and denominator. A fraction should be able to add itself to another fraction,
# returning a new fraction that represents the sum. A fraction should be able to multiply itself by another
# fraction, returning a new fraction as the product. A fraction should be able to take the reciprocal of
# itself, returning that value as a new fraction. A fraction should be able to simplify itself, returning
# a new fraction as that simplification.


class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def add(self, fraction):
        # cross multiply
        if self.denominator != fraction.denominator:
            # if denominators not the same look make them the same with cross multiplicaiton
            numer_1 = self.numerator * fraction.denominator
            numer_2 = fraction.numerator * self.denominator
            cmdn = fraction.denominator * self.denominator
            # add
            add_numer = numer_1 + numer_2
            new_fraction = Fraction(add_numer, cmdn)
            return new_fraction.simplify()
        else:
            new_fraction = Fraction((self.numerator + fraction.numerator), self.denominator)
            return new_fraction.simplify()

    def multiply(self, fraction):
        number_1 = self.numerator * fraction.numerator
        number_2 = self.denominator * fraction.denominator
        new_fraction = Fraction(number_1, number_2)
        return new_fraction.simplify()

    def simplify(self):
        gcf = 1

        counter = 2
        ender = self.numerator

        # find highest number to devide up to
        if self.numerator > self.denominator:
            ender = self.denominator

        # loop to find the GCF between numerator and denominator
        while counter < ender:
            if self.numerator % counter == 0 and self.denominator % counter == 0:
                gcf = counter
            counter += 1
        new_num = int(self.numerator / gcf)
        new_deno = int(self.denominator / gcf)
        new_simplification = Fraction(new_num, new_deno)
        return new_simplification

    def reciprocal(self):
        new_numerator = self.denominator
        new_denominator = self.numerator
        rep_fraction = Fraction(new_numerator, new_denominator)
        user_answer = input('Would you like to simplify the fraction if possible? ')
        if user_answer.lower() == 'yes':
            return rep_fraction.simplify()
        else:
            return rep_fraction

    def __repr__(self):
        return '%d / %d ' % (self.numerator, self.denominator)


a = Fraction(8, 10)
b = Fraction(2, 2)
a_mult = a.multiply(b)
add = a.add(b)
a_rep = a.reciprocal()
print(add)
print(a_mult.multiply(add))
print(a_rep)

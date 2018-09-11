# A student has a name and student ID number. A student can record grades and will
# track how many credits they have taken as well as their GPA. A student can also
# report what their class standing is (Freshman, Sophomore, Junior, Senior, Graduated)
# based on the number of credits they have taken.


class Student:

    def __init__(self, student_name, student_id, current_credits):
        self.name = student_name
        self.id = student_id
        self.credits = current_credits
        self.gpa = float(0)

    def class_standing(self):

        credits = self.credits

        if credits <= 23:
            return ('%s currently has %d credits so he has a class standing of Freshman' % (self.name, credits))
        elif 24 <= credits < 54:
            return ('%s currently has %d credits so he has a class standing of Sophomore' % (self.name, credits))
        elif 54 <= credits < 86:
            return ('%s currently has %d credits so he has a class standing of of Junior' % (self.name, credits))
        else:
            return ('%s currently has %d credits so he has a class standing of of Senior' % (self.name, credits))

    def add_credits(self, credit):
        # Freshman Standing (Level): fewer than 24 credits
        # Sophomore Standing (Level): at least 24 credits
        # Junior Standing (Level): at least 54 credits
        # Senior Standing (Level): at least 86 credits


james = Student('James John', 502932, 24)
print(james.class_standing())

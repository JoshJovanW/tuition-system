from classroom import Classroom
class Tutor:
    def __init__(self, name, age, subject, phoneNumber):
        self.name = name
        self.age = age
        self.subject = subject
        self.phoneNumber = phoneNumber
        self.classroom = ''

    def add_class_information(self, subject, charges, schedule):
        classroom = Classroom(subject, charges, schedule)
        self.classroom = classroom
        return "You have succesfully added the class information"

    def update_class_information(self, element, information):
        if self.classroom != '':
            self.classroom.update_information(element, information)

        else:
            return "Error, Class information has not been added. Please add the class information first."
        

    def view_profile(self):
        if self.classroom != '':
            self.classroom.see_students()

        else:
            return "Error, Class information has not been added. Please add the class information first."

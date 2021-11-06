class Classroom:
    def __init__(self, subject, price, schedule):
        self.subject = subject
        self.price = price
        self.schedule = schedule
        self.students = {}

    def update_information(self,element,input):
        if element == "price":
            self.price = int(input)
            return "You have succesfully updated the Price of this class"

        elif element == "schedule":
            self.schedule = input
            return "You have successfully updated the Class Schedule"

        elif element == "name":
            self.subject = input
            return "You have succesfully updated the Subject Name of this class"
          

    def see_students(self):
        if self.students != {}:
            print("Here are the list of students in this class : \n")
            for key, value in self.students:
                print(key, "  :  " , value)

        else:
            return "There are no enrollments in this class yet."

    def see_schedule(self):
        print("Here is your class schedule: \n")
        return self.schedule
                

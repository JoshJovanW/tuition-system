class Student:
    def __init__(self, name, ic, email, phoneNumber, address, grade, subjects):
        self.name = name
        self.ic = ic
        self.email = email
        self.phoneNumber = phoneNumber
        self.address = address
        self.grade = grade
        self.subjects = subjects
        self.payment = 0
        

    def update_information(self, element, input):
        if element == "email":
            self.email = input
            return "Your email has been updated"

        elif element == "phoneNumber":
            self.phoneNumber = input
            return "Your phoneNumber has been updated"
        
        elif element == "address":
            self.address = input
            return "your Address had been updated"

        else:
            return "Error, the element you wanted to update does not exist or is restricted. Please try again"

    def pay_tuition_fees(self, amount):
        self.payment += amount
    
    


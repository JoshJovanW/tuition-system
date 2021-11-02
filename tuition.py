staffId = 'staff' #Hard-coded staff Id and Password
staffPw = '12345'

def searchStudentPayment():
    print("\nSearch for payment made by Student\n"+"-"*30)

    paymentFile = open("payment.txt", "r")  #Open "payment.txt" and "student.txt" file in reading mode
    studentFile = open("student.txt", "r")

    print("Students:")
    for students in studentFile:  #Lists all the students names
        order = students.split("|")
        print("->", order[0])
    studentFile.close()

    found = False
    total = 0
    counter = 1
    studentName = input("\nEnter a student name: ")  #Prompt user for a student name
    for payment in paymentFile:
        order = payment.split("|")  #Splits strings in "payment.txt" based on the pipe symbol (|)
        if studentName == order[0]:  # If the name the user entered matches the name in the file, this if block will be executed
            if int(order[1])>0:  #order[1] is the amount paid, if the amount paid is >0, this if block will be executed
                print(str(counter)+". Paid Rm"+order[1], end="")  #Prints the amount paid by the student
                total += int(order[1])  #saves the total amount that have been paid by the student
                counter+=1
                found = True  #If the student name is found in the text file, found variable is set to True
    if found == True:  #If the found is True, the search is success, and the total amount of fees will be printed to the user
        paymentFile.close()
        print("\nSearch successfull, Total Paid = Rm"+str(total)+"\n\nReturning to Staff Menu~")
        staffMenu()
    elif found == False:  #If found is False (student name doesn't match the user input) It will prompt user to retry or go back to staff menu
        paymentFile.close()
        inp = input("\nUsername was not found or Student have never paid\nEnter 1 to Retry, or *any* to go back to Staff Menu: ")
        if inp == "1":
            searchStudentPayment()
        else:
            staffMenu()

def staffUpdateStudent():
    print("\nUpdate subject enrollment of a student\n"+"-"*30)

    studentFile = open("student.txt", "r")  # Open "student.txt" in read mode
    counter = 1
    for students in studentFile:  #'students' are the lines in "student.txt" file
        order = students.split("|")  #the lines are then split into variables where there are pipe symbol (|)
        print("["+str(counter)+"]", order[0])  #this code prints a number and order[0] which is the student names
        counter += 1
    studentFile.close()
    line = int(input("Select a student number : "))  #input for student list index
    
    studentData = ["name", "IC/Passport",  "email",     #studentData array to store student information
                   "phoneNum", "address", "level", 0, "subjects", 25000]
    studentFile = open("student.txt", "r")
    studentFileLine = studentFile.readlines()           #studentFile.readlines() turns "student.txt" into a list containing each lines
    print("Student Subject = " + order[7])

    newSubjects = input("\nEnter new subjects: ")
    studentFileLine[line-1] = studentData[0]+"|"+studentData[1]+"|"+studentData[2]+"|"+studentData[3]+"|"+studentData[4]+"|"+studentData[5]+"|"+str(studentData[6])+"|"+newSubjects+"\n"
    #The above sets the studentData with the correct index for the selected student, studentData are read from the readlines function, but the new subject is replaced with 'newSubjects' variable

    studentFile = open("student.txt", "w")  #Open "student.txt" in write mode (overwriting the whole file)
    studentFile.writelines(studentFileLine)  #but instead of overwriting the whole file, since writelines function is used, it only overwrites a whole line
    studentFile.close()
    
    print("\nStudent record successfully saved~\n\nReturning to Staff Menu")
    staffMenu()



def staffRegisterStudent():
    print("\nStudent Registration\n" + "-"*20)
    try:
        studentFile = open("student.txt", "a") #Open "student.txt" in append mode
        studentData = ["name", "IC/Passport",  "email", "phoneNum", "address", "level", 0, "subjects", 25000]  #Array to store Student Data #Note : 25000 = Default Student Fee
        studentData[0] = input("Student Name                    : ")
        studentData[1] = input("IC/Passport                     : ")
        studentData[2] = input("Student Email                   : ")
        studentData[3] = input("Contact Number                  : ")
        studentData[4] = input("Student Address                 : ")
        studentData[5] = input("Level                           : ")
        studentData[6] = int(input("Month of Enrollment(1-12)       : "))
        studentData[7] = input("Subjects(max 3)                 : ")

        studentFile.write(studentData[0]+"|"+studentData[1]+"|"+studentData[2]+"|"+studentData[3] +   #studentData array appended into "student.txt"
                          "|"+studentData[4]+"|"+studentData[5]+"|"+str(studentData[6])+"|"+studentData[7]+"|"+str(studentData[8])+"\n")
        studentFile.close()

        print("\nStudent Data successfully saved~\nReturning to Staff Menu")
        staffMenu()
    except:
        inp = input("\nAn Error Occured \nEnter '1' to Re-Do Register, or *any* to go back to Staff Menu: ")
        if inp == "1":
            staffRegisterStudent()
        else:
            print("Returning to Staff Menu~")
            staffMenu()

def staffRegisterTutor():
    print("\nTutor Registration\n" + "-"*18)
    try:
        tutorFile = open("tutor.txt", "a")  #Open "tutor.txt" in append mode
        tutorData = ["name", 69, "subject", "phoneNum"]  #Array to store tutor data to "tutor.txt"

        tutorData[0] = input("Tutor Name    : ")
        tutorData[1] = int(input("Tutor Age     : "))
        tutorData[2] = input("Subject       : ")
        tutorData[3] = input("Phone Number  : ")

        tutorFile.write(tutorData[0]+"|"+str(tutorData[1]) +"|"+tutorData[2]+"|"+tutorData[3]+"\n")  #tutorData array saved into "tutor.txt"
        tutorFile.close()
        print("\nTutor Data successfully saved~\nReturning to Staff Menu~")
        staffMenu()

    except:
        inp = input("An Error Occured \nEnter '1' to Re-Do Register, or *any* to go back to Staff Menu: ")
        if inp == "1":
            staffRegisterTutor()
        else:
            print("Returning to Staff Menu~")
            staffMenu()

def staffMenu():
    print("\nWelcome to Staff Menu\n" + "-" * 25)
    inp = 69
    while (inp < 0 or inp >4):  #Infinite loop, unless user inputs value 0-4
        inp = int(input("Select a Staff Menu: \n0. Go back to Main Menu\n1. Register a tutor \n2. Register a student\n3. Update a student subject\n4. Search Payment made by Student\n"))
    if inp == 0:
        mainMenu()
    elif inp == 1:
        staffRegisterTutor()
    elif inp == 2:
        staffRegisterStudent()
    elif inp == 3:
        staffUpdateStudent()
    elif inp == 4:
        searchStudentPayment()


def staffLogin():
    # Note: staffId and staffPw is hard-coded, staffId = 'staff' and staffPw = '12345'
    print("\nStaff Login, Enter 0 in Staff login ID to go back to Main Menu\n" + "-"*62)
    inpId = inpPw = ''
    login = False
    while True:  #This while loop looops forever unless the user enters the correct staff login ID and Password OR the user enters '0' in Staff Login ID
        inpId = input("Enter Staff login ID: ")
        inpPw = input("Enter Staff password: ")
        if(inpId == staffId and inpPw == staffPw):  #If the login ID and Password input correct, while loop will be broken and 'login' variabel is set to True
            login = True
            break
        elif(inpId == "0"):  #If user enters '0', while loop will be broken, but 'login' variable is set to False by default
            break
        else:
            print("\nIncorrect ID or Password, Please try again~\n")
    if (login):  #If the 'login' variable is True, user will be directed to staffMenu
        print("\nStaff login succesfull~")
        staffMenu()
    else:  #If user enters '0' instead, user will be directed to main menu
        mainMenu()

def mainMenu():
    print("\nMain Menu\n"+"-"*9)
    try:
        inp = 69
        while (inp < 1 or inp > 2):  #This loops forever unless the user input 1-2
            inp = int(input("Enter a number: \n1. Staff Login\n"))
        if inp == 1:
            staffLogin()
    except:
        print("\nInvalid Input Detected")
        mainMenu()

def studentLogin():
    print("\nStudent Login, Enter EXIT in studentName to go back to Main Menu\n" + "-"*62)

    studentFile = open("student.txt", "r")  # Open "student.txt" in read mode
    counter = 1
    for students in studentFile:  #'students' are the lines in "student.txt" file
        order = students.split("|")  #the lines are then split into variables where there are pipe symbol (|)
        print("["+str(counter)+"]", order[0])  #this code prints a number and order[0] which is the student names
        counter += 1
    studentFile.close()
    line = int(input("Select a student number : "))  #input for student list index

    studentData = ["name", "IC/Passport",  "email",     #studentData array to store student information
                   "phoneNum", "address", "level", 0, "subjects", 25000]
    studentFile = open("student.txt", "r")
    studentFileLine = studentFile.readlines()           #studentFile.readlines() turns "student.txt" into a list containing each lines
   
    studentFileLine[line-1] = studentData[0]+"|"+studentData[1]+"|"+studentData[2]+"|"+studentData[3]+"|"+studentData[4]+"|"+studentData[5]+"|"+str(studentData[6])+"|"+studentData[7]+"\n"
    #The above sets the studentData with the correct index for the selected student, studentData are read from the readlines function, but the new subject is replaced with 'newSubjects' variable

    studentFile = open("student.txt", "w")  #Open "student.txt" in write mode (overwriting the whole file)
    studentFile.writelines(studentFileLine)  #but instead of overwriting the whole file, since writelines function is used, it only overwrites a whole line
    studentFile.close()
    
    print("\nStudent record successfully saved~\n\nReturning to Staff Menu")
    staffMenu()



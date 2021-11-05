from program import Program
def main():
    running = True
    while running:
        print("\nMain Menu\n"+"-"*9)
        inp = int(input("Enter a number: 0. EXIT PROGRAM\n1. Staff Login\n2. Student Login\n3. Tutor Login\n"))
        
        program = Program()
        if inp == 1: 
            inpId = input("Enter Staff login ID: ")
            inpPw = input("Enter Staff password: ")
            print(program.staff_login(inpId, inpPw))
            
            if program.logged_in_as == 'staff':
                program.staff_menu()
        elif inp == 0:
            print("Thank you for using the program")
            running = False

        elif inp == 2:
            student_name = input("What is your name? ")
            print(program.student_login(student_name))

            if program.logged_in_as == 'student':
                program.student_menu()
        elif inp == 3:
            tutor_name = input("What is your name? ")
            print(program.tutor_login(tutor_name))
            
            if program.logged_in_as == 'tutor':
                program.tutor_menu()
           
main()

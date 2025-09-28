# student class to store student data as group
class Student:
    # worked with student id, name, department and enrollment status
    def __init__(self, id, name, dept, enroll):
        self.__id = id 
        self.__name = name 
        self.__dept = dept 
        self.__is_enrolled = enroll

    # enrolling a student
    def enroll_student(self):
        if self.__is_enrolled is not True: # if not enrolled yet: enroll it
            self.__is_enrolled = True
            print(f"{self.__id} is Enrolled Successfully")
        else: # if enrolled noting to do
            print("Already Enrolled")
    
    # dropping a student
    def drop_student(self):
        if self.__is_enrolled is True: # student only be dropped if enrolled once
            self.__is_enrolled = False
            print(f"{self.__id} is Dropped Successfully")
        else: # if already dropped noting to do
            print("Already Dropped")
    
    # text massage is create to represent the student data
    def view_student_info(self):
        text = f"ID: {self.__id}\nName: {self.__name}\nDept: {self.__dept}\nStatus: "
        if self.__is_enrolled is True:
            text += "Enrolled\n"
        else:
            text += "Not Enrolled\n"
        return text
    
    def __repr__(self):
        return self.view_student_info()

class StudentDatabase:
    student_list = [] # class attribute used to store all data

    def add_student(self, name, dept, enroll):
        self.id = len(self.student_list) + 101 # an id was given to each student
        student = Student(self.id, name, dept, enroll)
        self.student_list.append(student)

school = StudentDatabase()
school.add_student("Ridowan Ahmed", "CSE", True)
school.add_student("Malaika Cowdhuri", "CSE", False)
school.add_student("Concol Chowdhuri", "ME", False)
school.add_student("Sadia Ayman", "EEE", True)

while True:
    print("------------------Menu---------------")
    print("     1. View All Students")
    print("     2. Enroll Student")
    print("     3. Drop Student")
    print("     4. Exit")

    op = int(input("Enter the option: "))
    print("")

    if op == 1:
        print(*school.student_list)

    elif op == 2:
        try: # index error handled
            index = int(input("Enter Student id: "))-101
            school.student_list[index].enroll_student()
        except IndexError:
            print("Error: Student ID Not Exits")

    elif op == 3:
        try: # index error handled
            index = int(input("Enter Student id: "))-101
            school.student_list[index].drop_student()
        except IndexError:
            print("Error: Student ID Not Exits")
    
    elif op == 4:
        print("Exiting.............")
        break

    else:
        print("Enter Correct Credentials")
    
    print("")

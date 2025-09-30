# 2. Write a menu driven program to maintain student information. for every student
# store studetid, sname, and m1,m2,m3 marks for 3 subject. also store gpa in
# student list, add a function in student class to return GPA of a student
#  - Calculate GPA()
#       gpa=(1/3)*m1+(1/2)*m2+(1/4)*m3

# Create list to store Multiple students.
# 1. Display All Student
# 2. Search by id
# 3. Search by name
# 4. Calculate GPA of a student
# 5. Exit

# class Student:
    
#     def __init__(self,studetid,snmae,marks):
#         self._studetid = studetid
#         self._sname = snmae
#         self._marks = marks
    
#     def Calculate_gpa(self):
#         return (1/3)*self._marks['m1'] + (1/2)*self._marks['m2'] + (1/4)*self._marks['m3']
    
#     def __str__(self):
#         return f"Studentid : {self._studetid} , Name : {self._sname} , Marks : {self._marks}"

# def main():
#     student_information = []
    
#     while True:
#         print("\n------ MENU ------")
#         print("1. Add Student")
#         print("2. Display ")
#         print("3. Search by id")
#         print("4. Search by name")
#         print("5. Calculate GPA of a student")
#         print("6. Exit")
#         choice = int(input("Enter your choice: "))
        
#         if choice == 1:
#             id = int(input("Enter a student id "))
#             name = input("Enter Student Name ")
#             marks = {
#                     'm1': float(input("Enter marks in Subject 1: ")),
#                     'm2': float(input("Enter marks in Subject 2: ")),
#                     'm3': float(input("Enter marks in Subject 3: "))
#             }
            
#             student_information.append(Student(id,name,marks))
            
#         elif choice == 2:
#             for s in student_information:
#                 print(s)
            
#         elif choice == 6:
#             print("Exiting program...")
#             break
    

# if __name__ == "__main__":
#     main()

class Student:
    def __init__(self, studentid, sname, marks):
        self._studentid = studentid
        self._sname = sname
        self._marks = marks
        self._gpa = None 

    @property
    def studentid(self):
        return self._studentid

    @property
    def sname(self):
        return self._sname

    @property
    def marks(self):
        return self._marks

    @property
    def gpa(self):
        if self._gpa is None:
            self._gpa = self.calculate_gpa()
        return self._gpa

    def calculate_gpa(self):
        return (1/3) * self._marks['m1'] + (1/2) * self._marks['m2'] + (1/4) * self._marks['m3']

    def __str__(self):
        return f"Student ID: {self._studentid}, Name: {self._sname}, Marks: {self._marks}, GPA: {self.gpa:.2f}"


def main():
    student_information = []

    while True:
        print("\n------ MENU ------")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search by ID")
        print("4. Search by Name")
        print("5. Calculate GPA of a Student")
        print("6. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            studentid = int(input("Enter student ID: "))
            name = input("Enter student name: ")
            marks = {
                'm1': float(input("Enter marks in Subject 1: ")),
                'm2': float(input("Enter marks in Subject 2: ")),
                'm3': float(input("Enter marks in Subject 3: "))
            }
            student_information.append(Student(studentid, name, marks))
            print(f"Student {name} added successfully!")

        elif choice == 2:
            if student_information:
                for s in student_information:
                    print(s)
            else:
                print("No student records available.")

        elif choice == 3:
            search_id = int(input("Enter student ID to search: "))
            found = False
            for s in student_information:
                if s.studentid == search_id:
                    print(s)
                    found = True
                    break
            if not found:
                print("Student not found.")

        elif choice == 4:
            search_name = input("Enter student name to search: ")
            found = False
            for s in student_information:
                if s.sname.lower() == search_name.lower():
                    print(s)
                    found = True
            if not found:
                print("Student not found.")

        elif choice == 5:
            studentid = int(input("Enter student ID to calculate GPA: "))
            found = False
            for s in student_information:
                if s.studentid == studentid:
                    print(f"GPA of {s.sname} is: {s.gpa:.2f}")
                    found = True
                    break
            if not found:
                print("Student not found.")

        elif choice == 6:
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

# Q 1. Create a class 'Student' with rollno, studentName, course ,dictionary of
# marks(subjectName -> marks [5]). Provide following functionalities
# A. initializer
# B. override __str__ method
# C. accept student data
# D. Print student data for given id.
# E. Print Student who has failed in any subject. 

# Write menu driven program to test
# above functionalities.( accept records of 5 students and store those in list )


class Student:
    def __init__(self, rollno, studentName, course, marks):
        self.rollno = rollno
        self.studentName = studentName
        self.course = course
        self.marks = marks

    def __str__(self):
        return (f"Roll No: {self.rollno}, Name: {self.studentName}, "
                f"Course: {self.course}, Marks: {self.marks}")

    @staticmethod
    def accept_student():
        rollno = int(input("Enter Roll No: "))
        name = input("Enter Student Name: ")
        course = input("Enter Course: ")

        marks = {}
        print("Enter marks for 5 subjects:")
        for i in range(5):
            subject = input(f" Subject {i+1} name: ")
            mark = int(input(f" Marks in {subject}: "))
            marks[subject] = mark

        return Student(rollno, name, course, marks)

    def has_failed(self):
        """Check if student has failed in any subject (marks < 40)"""
        # Kas run hot aahe idk
        return any(mark < 40 for mark in self.marks.values())


def main():
    students = []

    print("Enter details of 1 students:")
    for _ in range(1):
        s = Student.accept_student()
        students.append(s)

    while True:
        print("\n------ MENU ------")
        print("1. Display all students")
        print("2. Display student by Roll No")
        print("3. Display students who failed in any subject")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("\nAll Students:")
            for s in students:
                print(s)

        elif choice == 2:
            roll = int(input("Enter Roll No to search: "))
            found = False
            for s in students:
                if s.rollno == roll:
                    print("\nStudent Found:")
                    print(s)
                    found = True
                    break
            if not found:
                print("No student with that Roll No.")

        elif choice == 3:
            print("\nStudents who failed in any subject:")
            failed_students = [s for s in students if s.has_failed()]
            if not failed_students:
                print("No student has failed in any subject.")
            else:
                for s in failed_students:
                    print(s)

        elif choice == 4:
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()

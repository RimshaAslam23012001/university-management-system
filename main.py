# University Management System (Enhanced OOP Version)

# Base class representing a generic person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

# Student class inheriting from Person
class Student(Person):
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self.rollNumber = roll_number  # Unique identifier for student
        self.courses = []  # List to hold registered courses

    # Method for student to register a course
    def registerCourse(self, course):
        if course not in self.courses:
            self.courses.append(course)
            course.addStudent(self)

# Instructor class inheriting from Person
class Instructor(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary  # Salary of the instructor
        self.courses = []  # Courses the instructor is assigned to

    # Assign instructor to a course
    def assignCourse(self, course):
        self.courses.append(course)
        course.setInstructor(self)

# Course class representing a university course
class Course:
    def __init__(self, course_id, name):
        self.id = course_id  # Unique course ID
        self.name = name
        self.students = []  # Students enrolled in this course
        self.instructor = None  # Instructor assigned to the course

    # Add a student to the course
    def addStudent(self, student):
        if student not in self.students:
            self.students.append(student)

    # Set instructor for the course
    def setInstructor(self, instructor):
        self.instructor = instructor

# Department class that holds a collection of courses
class Department:
    def __init__(self, name):
        self.name = name
        self.courses = []  # Courses in the department

    def addCourse(self, course):
        self.courses.append(course)

# University Management System to manage all entities
class UniversityManagementSystem:
    def __init__(self):
        self.students = []     # All registered students
        self.instructors = []  # All registered instructors
        self.courses = []      # All available courses

    # Add a new student
    def add_student(self, name, age, roll_number):
        student = Student(name, age, roll_number)
        self.students.append(student)
        print(f"Student {name} added.")

    # Add a new instructor
    def add_instructor(self, name, age, salary):
        instructor = Instructor(name, age, salary)
        self.instructors.append(instructor)
        print(f"Instructor {name} added.")

    # Add a new course
    def add_course(self, course_id, title):
        course = Course(course_id, title)
        self.courses.append(course)
        print(f"Course {title} added.")

    # Enroll a student in a course using roll number and course ID
    def enroll_student(self, roll_number, course_id):
        student = next((s for s in self.students if s.rollNumber == roll_number), None)
        course = next((c for c in self.courses if c.id == course_id), None)
        if student and course:
            student.registerCourse(course)
            print(f"Enrolled {student.name} in {course.name}.")
        else:
            print("Student or course not found.")

    # Assign an instructor to a course
    def assign_instructor(self, course_id, instructor_name):
        instructor = next((i for i in self.instructors if i.name == instructor_name), None)
        course = next((c for c in self.courses if c.id == course_id), None)
        if instructor and course:
            instructor.assignCourse(course)
            print(f"Instructor {instructor.name} assigned to {course.name}.")
        else:
            print("Instructor or course not found.")

    # Display list of all students
    def list_students(self):
        print("\nStudents:")
        for s in self.students:
            print(f"{s.rollNumber}: {s.name}, Age: {s.age}")

    # Display list of all courses along with assigned instructor
    def list_courses(self):
        print("\nCourses:")
        for c in self.courses:
            instructor_name = c.instructor.name if c.instructor else "None"
            print(f"{c.id}: {c.name} | Instructor: {instructor_name}")

    # Display student enrollments per course
    def list_enrollments(self):
        print("\nEnrollments:")
        for c in self.courses:
            for s in c.students:
                print(f"{s.name} -> {c.name}")

# Main function providing menu-driven CLI for user interaction
def main():
    ums = UniversityManagementSystem()
    while True:
        # Menu for operations
        print("\n1. Add Student\n2. Add Instructor\n3. Add Course\n4. Enroll Student\n5. Assign Instructor\n6. List Students\n7. List Courses\n8. List Enrollments\n9. Exit")
        choice = input("Enter choice: ")

        # Match user's choice with action
        if choice == '1':
            name = input("Name: ")
            age = int(input("Age: "))
            roll_number = input("Roll Number: ")
            ums.add_student(name, age, roll_number)
        elif choice == '2':
            name = input("Name: ")
            age = int(input("Age: "))
            salary = float(input("Salary: "))
            ums.add_instructor(name, age, salary)
        elif choice == '3':
            course_id = input("Course ID: ")
            title = input("Course Title: ")
            ums.add_course(course_id, title)
        elif choice == '4':
            roll_number = input("Student Roll Number: ")
            course_id = input("Course ID: ")
            ums.enroll_student(roll_number, course_id)
        elif choice == '5':
            instructor_name = input("Instructor Name: ")
            course_id = input("Course ID: ")
            ums.assign_instructor(course_id, instructor_name)
        elif choice == '6':
            ums.list_students()
        elif choice == '7':
            ums.list_courses()
        elif choice == '8':
            ums.list_enrollments()
        elif choice == '9':
            break
        else:
            print("Invalid choice.")

# Run the main program
if __name__ == "__main__":
    main()

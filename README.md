# 🎓 University Management System (Enhanced OOP Version)

A Python-based console application that simulates a simple **University Management System** using Object-Oriented Programming (OOP) concepts such as inheritance, encapsulation, and modular class design.

## 🧠 Features

- Add and manage students, instructors, and courses
- Enroll students in courses
- Assign instructors to courses
- View lists of:
  - All registered students
  - All available courses (with instructors)
  - Enrollments (which students are in which courses)
- Command-line interface (CLI) menu for user interaction

---

## 🏗️ OOP Structure

### ✅ Base Class: `Person`
- Attributes: `name`, `age`
- Inherited by: `Student`, `Instructor`

### ✅ Derived Class: `Student`
- Inherits from `Person`
- Attributes: `rollNumber`, `courses`
- Methods: `registerCourse(course)`

### ✅ Derived Class: `Instructor`
- Inherits from `Person`
- Attributes: `salary`, `courses`
- Methods: `assignCourse(course)`

### ✅ `Course`
- Attributes: `id`, `name`, `students`, `instructor`
- Methods: `addStudent(student)`, `setInstructor(instructor)`

### ✅ `Department`
- Attributes: `name`, `courses`
- Methods: `addCourse(course)`

### ✅ `UniversityManagementSystem`
- Manages all students, instructors, and courses
- Provides CLI operations for managing the system

---

## 💻 How to Run

1. Make sure Python is installed:  
   ```bash
   python --version

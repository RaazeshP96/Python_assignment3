'''
Create a console application for an IT Academy with the
following features:
    a) The academy program should have a fixed course of study.
    b) If a new student is interested in the academy program the student can
    inquiry about the course of study.
    c) Student Registration with Rs. 20000 (deposit). Students are allowed to
    pay in two installments with Rs. 10000 each.
    d) Display all the student’s information from the academy with their payments
    and remaining payments.
    e) Update the student information if needed.
    f) Delete the student information if he/she left the program.
    g) Return the deposit amount (Rs. 20000) to the students after the
    successful completion of the course and check the balance.

Remember it should be a full feature CONSOLE APP. You can store
the course of study and the student’s detail in your preferred file
format (.csv, .txt, etc).
Ignore the permissions for now. Anyone who runs the script is allowed to
access all the features. Develop the app with OOP Approach.

'''
import csv
import os


class Course:
    def __init__(self):
        with open('courses.csv', 'w', newline='') as file:
            field_names = ['courseid', 'course', 'time(hrs)']
            writer = csv.DictWriter(file, fieldnames=field_names)

            writer.writeheader()
            writer.writerow(
                {'courseid': '1', 'course': 'HtmlCss', 'time(hrs)': '60'})
            writer.writerow(
                {'courseid': '2', 'course': 'Js', 'time(hrs)': '90'})
            writer.writerow(
                {'courseid': '3', 'course': 'Python', 'time(hrs)': '90'})

    def course_read(self):
        with open('courses.csv', 'r', newline='') as file:
            read = csv.DictReader(file)
            for row in read:
                print(f"{row.get('courseid')} {row.get('course')}")


class Student:
    def __init__(self):
        self.field_names = ["name", "course", "deposit_status",
                            "deposit_amount_remaining", "paid_amount"]

    def new_student(self):
        name = input("Enter name:").lower()
        c1 = Course()
        c1.course_read()
        course = input("Enter a course name from above list:")
        print("Do you want to pay the full deposit of 20000 or 2 installment of 10000(Select 1 or 2):")
        print("1. Full deposit")
        print("2. 2 Installment of 1000")
        entry = int(input())
        if (entry == 2):
            deposit_status = "paid"
            amount_remaining = 0
            paid_amount = 20000

        elif (entry == 1):
            deposit_status = "half installment left"
            amount_remaining = 20000 - 10000
            paid_amount = 10000

        data = {"name": name, "course": course, "deposit_status": deposit_status,
                "deposit_amount_remaining": amount_remaining, "paid_amount": paid_amount}

        with open('students.csv', 'w+', newline='') as std_file:
            writer = csv.DictWriter(
                std_file, fieldnames=self.field_names)
            writer.writeheader()
            writer.writerow(data)

    def student_delete(self, name):
        with open('students.csv', "w", newline='') as writefile:
            writer = csv.DictWriter(writefile, fieldnames=self.field_names)
            with open('students.csv', 'r', newline='') as readfile:
                read = csv.DictReader(readfile)
                for row in read:
                    if row.get('name') != name:
                        writer.writerow(row)

    def student_update(self, name):
        with open('students.csv', 'r') as std_file:
            readdata = csv.DictReader(csv.DictReader(std_file))
            with open('students.csv', 'w') as std_file:
                writer = csv.DictWriter(
                    std_file, fieldnames=self.field_names)
                writer.writeheader()
                for row in readdata:
                    if (row.get('name') == name):
                        print("Update the info")
                        print('-'*30)
                        row['name'] = input("Enter the new name:").lower()
                        c1 = Course()
                        c1.course_read()
                        row['course'] = input(
                            "Enter a course name from above list:")
                        print(
                            "Do you want to pay the full deposit of 20000 or 2 installment of 10000(Select 1 or 2):")
                        print("1. Full deposit")
                        print("2. 2 Installment of 1000")
                        entry = int(input())
                        if (entry == 2):
                            row['deposit_status'] = "paid"
                            row['amount_remaining'] = 0
                            row['paid_amount'] = 20000

                        elif (entry == 1):
                            row['deposit_status'] = "half installment left"
                            row['amount_remaining'] = 20000 - 10000
                            row['paid_amount'] = 10000
                    writer.writerow(row)

    def student_read(self):
        with open('students.csv', 'r', newline='') as std_file:
            read = csv.DictReader(std_file)
            for row in read:
                print(row)


# main

# for student registration
class Academy(Course, Student):
    def __init__(self):
        Course.__init__(self)
        Student.__init__(self)

    def menu(self):
        print("Our Menu")
        print('-'*30)
        print("1. New Student Registration")
        print("2. View All Student")
        print("3. Update student info")
        print("4. Delete Student")

        itemnum = int(
            input("Please enter the number of menu item you want to access:"))

        if (itemnum == 1):
            self.new_student()

        elif (itemnum == 2):
            self.student_read()

        elif (itemnum == 3):
            input_data = input(
                "Enter the name of student you want to update:").lower()
            self.student_update(input_data)

        elif (itemnum == 4):
            input_data = input(
                "Enter the name of student to you want to delete:")
            self.student_delete(input_data)

        else:
            print("Invalid input")


obj1 = Academy()
obj1.menu()

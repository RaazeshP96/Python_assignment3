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


class Course:
    def course_write(self):
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
                print(row.get('course'))


class Student:
    def __init__(self, name, course, paid, unpaid):
        self.name = name
        self.course = course
        self.paid = paid
        self.unpaid = unpaid

    def student_write(self):
        with open('student.csv', "w", newline='') as file:
            field_names = ['name', 'course', 'paid', 'unpaid']
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writeheader()
            writer.writerow(
                {'name': self.name, 'course': self.course, 'paid': self.paid, "unpaid": self.unpaid})

    def student_delete(self):
        with open('student.csv', "w", newline='') as writefile:
            field_names = ['name', 'course', 'paid', 'unpaid']
            writer = csv.DictWriter(writefile, fieldnames=field_names)
            with open('student.csv', 'r', newline='') as readfile:
                read = csv.DictReader(readfile)
                for row in read:
                    if row.get('name') != self.name:
                        writer.writerow(row)

    def student_update(self):
        with open('student.csv', "w", newline='') as writefile:
            field_names = ['name', 'course', 'paid', 'unpaid']
            writer = csv.DictWriter(writefile, fieldnames=field_names)
            with open('student.csv', 'r', newline='') as readfile:
                read = csv.DictReader(readfile)
                for row in read:
                    if row.get('name') != self.name:
                        writer.writerow(row)
                    else:
                        writer.writerow(
                            {'name': self.name, 'course': self.course, 'paid': self.paid, "unpaid": self.unpaid})

    def student_read(self):
        with open('student.csv', 'r', newline='') as stdfile:
            read = csv.DictReader(stdfile)
            for row in read:
                print(row)


# main

# for student registration
c1 = Course()
c1.course_write()
name = input("Enter the name:")
print('-'*30)
print("our available courses")
c1.course_read()
print('-'*30)
enroll = (input("Do you want to enroll (y/n):")).lower()
if enroll == 'y':
    course = (input("Enter the course you want to enroll:")).lower()
    paid = int(input("Diposite 10000 or 20000:"))
    unpaid = 20000-paid
    s1 = Student(name, course, paid, unpaid)
    s1.student_write()
    print('-'*30)
    print("You are enrolled!!!")
    print('-'*30)
    s1.student_read()


# deletion of student
# s2=Student('rita',"js",'10000','10000')
# s2.student_delete()

# update of student
# s2=Student('rita',"js",'10000','10000')
# s2.student_update()

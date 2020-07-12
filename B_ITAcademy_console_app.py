# B. Create a console application for an IT Academy with the
# following features:
# a) The academy program should have a fixed course of study.
# b) If a new student is interested in the academy program the student can
# inquiry about the course of study.
# c) Student Registration with Rs. 20000 (deposit). Students are allowed to
# pay in two installments with Rs. 10000 each.
# d) Display all the student’s information from the academy with their payments
# and remaining payments.
# e) Update the student information if needed.
# f) Delete the student information if he/she left the program.
# g) Return the deposit amount (Rs. 20000) to the students after the
# successful completion of the course and check the balance.
# Remember it should be a full feature CONSOLE APP. You can store
# the course of study and the student’s detail in your preferred file
# format (.csv, .txt, etc).
# Ignore the permissions for now. Anyone who runs the script is allowed to
# access all the features. Develop the app with OOP Approach.


# For this console app, we maintain two csv files which are always in sync with each other
# We have a separate txt file for storing information about the academy and course of study

import csv

class ItAcademy:

    def __init__(self, full_name, email, phone, payment):
        self.full_name = full_name
        self.payment = payment
        self.email = email
        self.phone = phone
        # to find the last id
        with open('academy.csv') as f:
            reader = list(csv.reader(f))
            id = reader[-1][0]
            if id == 'ID':
                id = 0
            else:
                id = int(reader[-1][0]) + 1
        due = 0 if self.payment == '20000' else '10000'
        with open('academy.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([id, self.full_name, self.email, self.phone, self.payment, due])
        with open('academy1.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([id, self.full_name, self.email, self.phone, self.payment, due])
        print("Registration successful.")
    @staticmethod
    def inquire(inquiry):
        print("Thank you for the query. Please go through the following details about the program until we get back to you.\n")
        with open('course.txt', 'r') as f:
            content = f.read()
            print(content)

    # show information of a single student
    @staticmethod
    def show_std_info(std_id):
        with open('academy.csv') as f:
            reader = csv.DictReader(f)
            flag = 0
            for dict1 in reader:
                if dict1['ID'] == std_id:
                    flag = 1
                    print("ID: ", dict1['ID'])
                    print(f"Name: {dict1['Full Name']}")
                    print(f"Email: {dict1['Email']}")
                    print(f"Phone: {dict1['Phone']}")
                    print("Payment: ", dict1['Payment'])
                    print("Due: ", dict1['Due'])
                    break
            if not flag:
                print("ID does not exist.")

    # show information of all students
    @staticmethod
    def show_all_stds():
        with open('academy.csv') as f:
            reader = csv.DictReader(f)
            print("ID\tFull Name\tEmail\t\tPhone\t\tPayment\tDue\n")
            for line in reader:
                for value in line.values():
                    print(value, end='\t')
                print(end='\n')

    # update student information
    @staticmethod
    def update_std_info(std_id, key, value):
        with open('academy.csv', 'r') as f:
            reader = csv.DictReader(f)
            for line_num,line in enumerate(reader):
                if line['ID'] == std_id:
                    break
            line[key] = value
        with open('academy.csv', 'r') as f:
            reader = csv.DictReader(f)
            with open('academy1.csv','w') as file:
                field_names = ['ID', 'Full Name', 'Email', 'Phone', 'Payment', 'Due']
                writer = csv.DictWriter(file, field_names)
                writer.writeheader()
                for i,row in enumerate(reader):
                    if i == line_num:
                        writer.writerow(line)
                    else:
                        writer.writerow(row)
        with open('academy1.csv', 'r') as f:
            reader = csv.DictReader(f)
            with open('academy.csv','w') as file:
                field_names = ['ID', 'Full Name', 'Email', 'Phone', 'Payment', 'Due']
                writer = csv.DictWriter(file, field_names)
                writer.writeheader()
                for row in reader:
                    writer.writerow(row)
        print("Update successful.")

    @staticmethod
    def delete_std(std_id):
        with open('academy.csv', 'r') as f:
            reader = csv.DictReader(f)
            with open('academy1.csv','w') as file:
                field_names = ['ID', 'Full Name', 'Email', 'Phone', 'Payment', 'Due']
                writer = csv.DictWriter(file, field_names)
                writer.writeheader()
                for row in reader:
                    if row['ID'] == std_id:
                        continue
                    else:
                        writer.writerow(row)
        with open('academy1.csv', 'r') as f:
            reader = csv.DictReader(f)
            with open('academy.csv','w') as file:
                field_names = ['ID', 'Full Name', 'Email', 'Phone', 'Payment', 'Due']
                writer = csv.DictWriter(file, field_names)
                writer.writeheader()
                for row in reader:
                    writer.writerow(row)
        print("Student information deleted.")

    @staticmethod
    def return_deposit(std_id):
        with open('academy.csv', 'r') as f:
            reader = csv.DictReader(f)
            for line_num,line in enumerate(reader):
                if line['ID'] == std_id:
                    break
            if line['Payment'] == '10000':
                print("You still have due of 10000.")
                return
            line['Payment'] = 'Deposit Returned'
        with open('academy.csv', 'r') as f:
            reader = csv.DictReader(f)
            with open('academy1.csv','w') as file:
                field_names = ['ID', 'Full Name', 'Email', 'Phone', 'Payment', 'Due']
                writer = csv.DictWriter(file, field_names)
                writer.writeheader()
                for i,row in enumerate(reader):
                    if i == line_num:
                        writer.writerow(line)
                    else:
                        writer.writerow(row)
        with open('academy1.csv', 'r') as f:
            reader = csv.DictReader(f)
            with open('academy.csv','w') as file:
                field_names = ['ID', 'Full Name', 'Email', 'Phone', 'Payment', 'Due']
                writer = csv.DictWriter(file, field_names)
                writer.writeheader()
                for row in reader:
                    writer.writerow(row)
        print("Deposit returned to the student.")

    @staticmethod
    def pay_second_installment(std_id):
        with open('academy.csv', 'r') as f:
            reader = csv.DictReader(f)
            for line_num,line in enumerate(reader):
                if line['ID'] == std_id:
                    break
            if line['Payment'] == '20000':
                print("You have paid full.")
                return
            if line['Payment'] == 'Deposit Returned':
                print("You have already completed course.")
                return
            line['Payment'] = 20000
            line['Due'] = 0
        with open('academy.csv', 'r') as f:
            reader = csv.DictReader(f)
            with open('academy1.csv','w') as file:
                field_names = ['ID', 'Full Name', 'Email', 'Phone', 'Payment', 'Due']
                writer = csv.DictWriter(file, field_names)
                writer.writeheader()
                for i,row in enumerate(reader):
                    if i == line_num:
                        writer.writerow(line)
                    else:
                        writer.writerow(row)
        with open('academy1.csv', 'r') as f:
            reader = csv.DictReader(f)
            with open('academy.csv','w') as file:
                field_names = ['ID', 'Full Name', 'Email', 'Phone', 'Payment', 'Due']
                writer = csv.DictWriter(file, field_names)
                writer.writeheader()
                for row in reader:
                    writer.writerow(row)
        print("Second installment paid.")


print("To register as a new student, enter 1.")
print("To inquire about the program and course of study, enter 2.")
print("To see information of all students, enter 3.")
print("To see information of a single student, enter 4.")
print("To update information of a student, enter 5.")
print("To delete student information who has left the program, enter 6.")
print("To pay second installment, enter 7.")
print("To return deposit after successful completion of course, enter 8.")

n = int(input())

if n == 1:
    name = input("Enter full name: ")
    email = input("Enter email: ")
    phone = input("Enter phone: ")
    payment = input("Enter payment: ")
    # ItAcademy("Dev Adhikari", 'dev@dev.com', '1231231230', 1000)
    ItAcademy(name, email, phone, payment)
elif n == 2:
    inquiry = input("Enter your inquiry: ")
    ItAcademy.inquire(inquiry)
elif n == 3:
    ItAcademy.show_all_stds()
elif n == 4:
    std_id = input("Enter student's ID: ")
    ItAcademy.show_std_info(std_id)
elif n == 5:
    std_id = input("Enter student's ID: ")
    print("To change name, enter 1.")
    print("To change email, enter 2.")
    print("To change phone, enter 3.")
    m = int(input())
    if m == 1:
        key = 'Full Name'
    elif m == 2:
        key = 'Email'
    elif m == 3:
        key = 'Phone'
    else:
        exit("Not valid input.")
    value = input("Enter what you want it to change to: ")
    ItAcademy.update_std_info(std_id, key, value)
elif n == 6:
    std_id = input("Enter student's ID: ")
    ItAcademy.delete_std(std_id)
elif n == 7:
    std_id = input("Enter student's ID: ")
    ItAcademy.pay_second_installment(std_id)
elif n == 8:
    std_id = input("Enter student's ID: ")
    ItAcademy.return_deposit(std_id)
else:
    exit("Invalid input.")

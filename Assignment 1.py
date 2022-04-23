#Q1. Average of three numbers entered by user

n1 = int(input(" Please Enter the First Number: "))
n2 = int(input(" Please Enter the second number: "))
n3 = int(input(" Please Enter the third number: "))
avg=(n1 + n2 + n3)/3
print("The average of three numbers is ", avg)

#Q2.Computing person's income tax

gross_income = float(input("Enter your gross income"))
number_of_dependents = float(input("Enter number of dependents"))
std_deduction = 10000
tax_income = gross_income - std_deduction -(number_of_dependents * 3000)
tax = (tax_income * 20)/100
if(tax<0):
    print("Invalid input")
else:
    print("Tax:", tax)

#Q3.Storing different data type values into a list
        
SID = input("Enter your SID: ")
Name = input("Enter your Name: ")
Gender = input("Enter your Gender: ")
Course_Name = input("Enter your Course Name: ")
CGPA = input("Enter your CGPA: ")
Student = [SID, Name, Gender, Course_Name, CGPA]
print("Student:",Student)

#Q4.Marks of 5 Students

m1 = int(input("Marks of 1st student: "))
m2 = int(input("Marks of 2nd student: "))
m3 = int(input("Marks of 3rd student: "))
m4 = int(input("Marks of 4th student: "))
m5 = int(input("Marks of 5th student: "))
SortedMarks = [m1, m2, m3, m4, m5]
print(SortedMarks)

#Q5(a).Removing 4th element

List_of_colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'yellow']
print("List of colors before removing: ", List_of_colors)
List_of_colors.pop(3)
print("your list after removing 4th element: ",List_of_colors)

#Q5(b).Replacing Black and Pink with Purple

List_of_colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print("List of colors before replacing:",List_of_colors)
List_of_colors[3:5]= ['Purple']
print("your list after replacing black and pink with purple:", List_of_colors)



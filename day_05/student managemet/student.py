student={}
while True:
    print("\n 1. To enter a new Student.")
    print("\n 1. To enter a new Student.")
    print("2. To update student data.")
    print("3. To delet student data.")
    print("4. To check the status of student.")
    print("5. Exit.")

    chose=int(input("\n Enter your number--"))

# enter new student
    if chose == 1:
        rollno =int(input("\n Enter the rollno of the Student-->"))
        name =input("Enter the Name of the Student-->")
        course=input("Enter the course name of the student-->")
       
        student[rollno]={
            "Name": name,
            "Course":course
        }
        print("Data is Entered sucessfully.")

# update student
    elif chose ==2:
        rollno =int(input("\n Enter the rollno of update Student data-->"))
        if rollno in student:
            course=input("Enter the updated course name of the student-->")
            student[rollno]["Course"]= course
            print("successfull update the student data")
        else:
                print("student is not found.")

# check status student
    elif chose ==3:
        rollno =int(input("\n Enter the rollno of update Student data-->"))
        if rollno in student:
                del student[rollno]
                print("successfully remove the student data.")
        else:
            print("\n Student is not found.")

#check the status
    elif chose ==4:
            rollno =int(input("\n Enter the rollno to show the Student status-->"))
            if rollno in student:
                print("\n student details are following")
                print("rollno of the student is -->",rollno)
                print("Name of the Student-->",student[rollno]["Name"])
                print("Name of the Student-->",student[rollno]["Course"])
            else:
                print("\n Student is not found.")
                
#break or exit the loop
    elif chose==5:
        print("Thank you")
        break                
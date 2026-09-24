
#===== STUDENT MANAGEMENT SYSTEM ===== 


students=dict()

#add student
def AddStudent():
     while True:
            print()
            id=input("Enter ID: ")
            if id in students:
                print("ID already Exist.")
            else:
                each_dict=dict()
                each_dict["id"]=id
                students[id]=each_dict
                
                name=input("Enter Name: ")
                students[id]["name"]=name
                #students[id]=each_dict

                Age=input("Enter Age: ")
                students[id]["Age"]=Age

                Course=input("Enter Course: ")
                students[id]["Course"]=Course

                break

#view student list
def ViewStudent():
    for student in students.values():
        print("ID:", student["id"]+",", "Name:", student["name"]+",", "Age:", student["Age"]+",", "Course:", student["Course"]+",")


#Search Student
def SearchStudent():
    search=input("Enter Student ID: ")
    if search in students:
        print("Name:", students[search]["name"]+",", "Age:", students[search]["Age"]+",", "Course:", students[search]["Course"]+",")
    else:
        print("Not Found")


# Update Student
def UpdateStudent():
    id=input("Enter Student ID: ")
    if id in students:
        print("Name:", students[id]["name"]+",", "Age:", students[id]["Age"]+",", "Course:", students[id]["Course"]+",")
        
        each_dict=dict()
        each_dict["id"]=id
        students[id]=each_dict
                
        name=input("Enter Name: ")
        students[id]["name"]=name
        #students[id]=each_dict

        Age=input("Enter Age: ")
        students[id]["Age"]=Age

        Course=input("Enter Course: ")
        students[id]["Course"]=Course
    else:
        print("Not Found")

#DeleteStudent
def DeleteStudent():
    del_std=input("Enter student ID to Delete: ")
    if del_std in students:
        del students[del_std]
    else:
        print("Not Found")


while True:
    print("1. Add Student: ")
    print("2. View Students: ")
    print("3. Search Student: ")
    print("4. Update Student: ")
    print("5. Delete Student: ")
    print("6. Exit: ")

    choice=input("Enter the NUMBER of your choice...: ")

    if choice=="1":
        while True:
            AddStudent()
            another=input("Add another Student? N to Exit ENTER to continue: ")
            if another.lower()=="n":
                break

    elif choice=="2":
        while True:
            ViewStudent()
            print()
            another=input("Type N to Exit: ")
            if another.lower()=="n":
                break
    elif choice=="3":
        while True:
            SearchStudent()
            print()
            another=input("Type N to Exit")
            if another.lower()=="n":
                break
    elif choice=="4":
        while True:
            UpdateStudent()
            print()
            another=input("Type N to Exit: ")
            if another.lower()=="n":
                break
    elif choice=="5":
        while True:
            DeleteStudent()
            print("Successfully eleted")
            print()
            another=input("Type N to Exit: ")
            if another.lower()=="n":
                break
    elif choice=="6":
        print()
        print("You have EXITED!")
        break
    else:
        print()
        print("Use the correct number!")
    

    #print(students)


    #break
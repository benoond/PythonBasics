
expenses=[]

'''
while True:
    qn=input("Do you want to add another expense? (yes/no): ")
    if qn.lower()=="yes": '''
number_of_times=0
divisor=0
while True:
    num_of_exp=input("How many expenses do you want to enter? ")
    if not num_of_exp.isdigit():
        print("Please Enter number")
    elif int(num_of_exp)<1:
        print("number of expenses must be more than 0")
        break
    else:
        number_of_times=int(num_of_exp)
        divisor=number_of_times
        break

current=1
while number_of_times >0:
    exp=int(input(f"Enter expense {current}: "))
    expenses.append(exp)
    current+=1
    number_of_times -=1

if divisor>0:
    print()
    print(f"Total spent: {sum(expenses)}")
    print(f"Average expense: {sum(expenses)/divisor}")
    print(f"Highest expense: {max(expenses)}")
    print(f"Lowest expense: {min(expenses)}")